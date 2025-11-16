"""
Test suite for Synapse Registry API
Unit and integration tests for all registry endpoints

Author: Synapse Team
License: MIT
"""

import pytest
import json
import base64
import tarfile
import io
from pathlib import Path
import sys

# Add synapse-registry to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'synapse-registry'))

from app import app, db
from models import User, Package, PackageVersion
from auth import hash_password, generate_token
from storage import create_package_tarball


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


@pytest.fixture
def test_user(client):
    """Create test user"""
    with app.app_context():
        user = User(
            username='testuser',
            email='test@example.com',
            password_hash=hash_password('TestPassword123!')
        )
        db.session.add(user)
        db.session.commit()
        return user


@pytest.fixture
def auth_token(test_user):
    """Generate auth token for test user"""
    return generate_token(test_user.id)


def create_test_package_tarball(name: str, version: str) -> bytes:
    """Create a test package tarball"""
    manifest = {
        'name': name,
        'version': version,
        'description': f'Test package {name}',
        'author': 'testuser',
        'license': 'MIT',
        'dependencies': {}
    }
    
    # Create tarball in memory
    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode='w:gz') as tar:
        # Add manifest
        manifest_data = json.dumps(manifest).encode()
        info = tarfile.TarInfo(name='synapse.json')
        info.size = len(manifest_data)
        tar.addfile(info, io.BytesIO(manifest_data))
        
        # Add dummy source file
        source_data = b'let x = 42'
        info = tarfile.TarInfo(name=f'{name}.syn')
        info.size = len(source_data)
        tar.addfile(info, io.BytesIO(source_data))
    
    return tar_buffer.getvalue()


# ============================================================================
# Authentication Tests
# ============================================================================

class TestAuthentication:
    """Authentication endpoint tests"""
    
    def test_register_success(self, client):
        """Test successful user registration"""
        response = client.post('/api/v1/auth/register', json={
            'username': 'newuser',
            'password': 'NewPassword123!',
            'email': 'new@example.com'
        })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['success'] is True
        assert data['user']['username'] == 'newuser'
    
    def test_register_missing_fields(self, client):
        """Test registration with missing fields"""
        response = client.post('/api/v1/auth/register', json={
            'username': 'newuser'
        })
        assert response.status_code == 400
    
    def test_register_duplicate_username(self, client, test_user):
        """Test registration with existing username"""
        response = client.post('/api/v1/auth/register', json={
            'username': 'testuser',
            'password': 'Password123!',
            'email': 'different@example.com'
        })
        assert response.status_code == 409
    
    def test_login_success(self, client, test_user):
        """Test successful login"""
        response = client.post('/api/v1/auth/login', json={
            'username': 'testuser',
            'password': 'TestPassword123!'
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert 'token' in data
        assert data['user']['username'] == 'testuser'
    
    def test_login_invalid_credentials(self, client, test_user):
        """Test login with wrong password"""
        response = client.post('/api/v1/auth/login', json={
            'username': 'testuser',
            'password': 'WrongPassword123!'
        })
        assert response.status_code == 401
    
    def test_verify_token_valid(self, client, auth_token):
        """Test token verification with valid token"""
        response = client.post('/api/v1/auth/verify', json={
            'token': auth_token
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['valid'] is True
        assert 'user' in data
    
    def test_verify_token_invalid(self, client):
        """Test token verification with invalid token"""
        response = client.post('/api/v1/auth/verify', json={
            'token': 'invalid.token.here'
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['valid'] is False


# ============================================================================
# Package Publishing Tests
# ============================================================================

class TestPublishing:
    """Package publishing endpoint tests"""
    
    def test_publish_success(self, client, auth_token):
        """Test successful package publication"""
        tarball = create_test_package_tarball('test-package', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        response = client.post(
            '/api/v1/packages',
            json={
                'name': 'test-package',
                'version': '1.0.0',
                'description': 'A test package',
                'author': 'testuser',
                'license': 'MIT',
                'tarball': tarball_b64,
                'keywords': ['test', 'demo'],
                'dependencies': {}
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['success'] is True
        assert data['package']['name'] == 'test-package'
        assert data['package']['version'] == '1.0.0'
    
    def test_publish_requires_auth(self, client):
        """Test that publishing requires authentication"""
        tarball = create_test_package_tarball('test-package', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        response = client.post('/api/v1/packages', json={
            'name': 'test-package',
            'version': '1.0.0',
            'description': 'A test package',
            'tarball': tarball_b64,
        })
        
        assert response.status_code == 401
    
    def test_publish_invalid_package_name(self, client, auth_token):
        """Test publishing with invalid package name"""
        tarball = create_test_package_tarball('INVALID-NAME', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        response = client.post(
            '/api/v1/packages',
            json={
                'name': 'INVALID-NAME',
                'version': '1.0.0',
                'description': 'Test',
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        assert response.status_code == 400
    
    def test_publish_invalid_version(self, client, auth_token):
        """Test publishing with invalid version format"""
        tarball = create_test_package_tarball('test-package', 'invalid')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        response = client.post(
            '/api/v1/packages',
            json={
                'name': 'test-package',
                'version': 'invalid',
                'description': 'Test',
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        assert response.status_code == 400
    
    def test_publish_duplicate_version(self, client, auth_token):
        """Test publishing duplicate version"""
        tarball = create_test_package_tarball('test-package', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        # First publish
        client.post(
            '/api/v1/packages',
            json={
                'name': 'test-package',
                'version': '1.0.0',
                'description': 'Test',
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        # Try to publish again
        response = client.post(
            '/api/v1/packages',
            json={
                'name': 'test-package',
                'version': '1.0.0',
                'description': 'Test',
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        assert response.status_code == 409


# ============================================================================
# Package Discovery Tests
# ============================================================================

class TestDiscovery:
    """Package discovery endpoint tests"""
    
    def test_get_package(self, client, auth_token):
        """Test getting package metadata"""
        # Publish a package first
        tarball = create_test_package_tarball('test-package', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        client.post(
            '/api/v1/packages',
            json={
                'name': 'test-package',
                'version': '1.0.0',
                'description': 'Test package',
                'author': 'testuser',
                'license': 'MIT',
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        # Get package
        response = client.get('/api/v1/packages/test-package')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['name'] == 'test-package'
        assert len(data['versions']) == 1
        assert data['versions'][0]['version'] == '1.0.0'
    
    def test_get_nonexistent_package(self, client):
        """Test getting nonexistent package"""
        response = client.get('/api/v1/packages/nonexistent')
        assert response.status_code == 404
    
    def test_get_specific_version(self, client, auth_token):
        """Test getting specific package version"""
        tarball = create_test_package_tarball('test-package', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        client.post(
            '/api/v1/packages',
            json={
                'name': 'test-package',
                'version': '1.0.0',
                'description': 'Test package',
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        response = client.get('/api/v1/packages/test-package/1.0.0')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['version'] == '1.0.0'
        assert data['name'] == 'test-package'
    
    def test_list_versions(self, client, auth_token):
        """Test listing all versions"""
        # Publish multiple versions
        for version in ['1.0.0', '1.1.0', '2.0.0']:
            tarball = create_test_package_tarball('test-package', version)
            tarball_b64 = base64.b64encode(tarball).decode()
            
            client.post(
                '/api/v1/packages',
                json={
                    'name': 'test-package',
                    'version': version,
                    'description': 'Test',
                    'tarball': tarball_b64,
                },
                headers={'Authorization': f'Bearer {auth_token}'}
            )
        
        response = client.get('/api/v1/packages/test-package/versions')
        assert response.status_code == 200
        
        data = response.get_json()
        assert len(data['versions']) == 3
        assert '1.0.0' in data['versions']
        assert '2.0.0' in data['versions']
    
    def test_search_packages(self, client, auth_token):
        """Test package search"""
        # Publish a package
        tarball = create_test_package_tarball('graph-lib', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        client.post(
            '/api/v1/packages',
            json={
                'name': 'graph-lib',
                'version': '1.0.0',
                'description': 'Graph algorithms',
                'author': 'testuser',
                'keywords': ['graph', 'algorithms'],
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        response = client.get('/api/v1/search?q=graph')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['total'] >= 1
        assert len(data['results']) >= 1


# ============================================================================
# Download & Tarball Tests
# ============================================================================

class TestDownloads:
    """Download and tarball endpoint tests"""
    
    def test_download_tarball(self, client, auth_token):
        """Test downloading package tarball"""
        tarball = create_test_package_tarball('test-package', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        client.post(
            '/api/v1/packages',
            json={
                'name': 'test-package',
                'version': '1.0.0',
                'description': 'Test',
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        
        response = client.get('/api/v1/packages/test-package/1.0.0/tarball')
        assert response.status_code == 200
        assert response.content_type == 'application/gzip'
    
    def test_download_nonexistent_tarball(self, client):
        """Test downloading nonexistent tarball"""
        response = client.get('/api/v1/packages/nonexistent/1.0.0/tarball')
        assert response.status_code == 404


# ============================================================================
# Statistics Tests
# ============================================================================

class TestStatistics:
    """Statistics endpoint tests"""
    
    def test_get_stats(self, client, auth_token):
        """Test getting registry statistics"""
        # Publish some packages
        for i in range(3):
            tarball = create_test_package_tarball(f'package-{i}', '1.0.0')
            tarball_b64 = base64.b64encode(tarball).decode()
            
            client.post(
                '/api/v1/packages',
                json={
                    'name': f'package-{i}',
                    'version': '1.0.0',
                    'description': f'Package {i}',
                    'tarball': tarball_b64,
                },
                headers={'Authorization': f'Bearer {auth_token}'}
            )
        
        response = client.get('/api/v1/stats')
        assert response.status_code == 200
        
        data = response.get_json()
        assert 'packages' in data
        assert data['packages']['total'] >= 3


# ============================================================================
# Health Check Tests
# ============================================================================

class TestHealth:
    """Health check endpoint tests"""
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get('/api/v1/health')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert 'timestamp' in data
        assert 'version' in data


# ============================================================================
# Integration Tests
# ============================================================================

class TestIntegration:
    """End-to-end integration tests"""
    
    def test_full_workflow(self, client, auth_token):
        """Test complete publish-discover-download workflow"""
        # 1. Publish package
        tarball = create_test_package_tarball('workflow-test', '1.0.0')
        tarball_b64 = base64.b64encode(tarball).decode()
        
        pub_response = client.post(
            '/api/v1/packages',
            json={
                'name': 'workflow-test',
                'version': '1.0.0',
                'description': 'Workflow test package',
                'author': 'testuser',
                'keywords': ['test', 'workflow'],
                'tarball': tarball_b64,
            },
            headers={'Authorization': f'Bearer {auth_token}'}
        )
        assert pub_response.status_code == 201
        
        # 2. Discover package
        disc_response = client.get('/api/v1/packages/workflow-test')
        assert disc_response.status_code == 200
        disc_data = disc_response.get_json()
        assert disc_data['name'] == 'workflow-test'
        
        # 3. Download tarball
        dl_response = client.get('/api/v1/packages/workflow-test/1.0.0/tarball')
        assert dl_response.status_code == 200
        
        # 4. Search
        search_response = client.get('/api/v1/search?q=workflow')
        assert search_response.status_code == 200
        search_data = search_response.get_json()
        assert search_data['total'] >= 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
