"""
Synapse Package Registry - REST API Server
Flask-based REST API for package publishing, discovery, and management

Author: Synapse Team
License: MIT
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from functools import wraps
import json
import os
import hashlib
import logging
from datetime import datetime, timedelta
from typing import Dict, Tuple, List, Optional
import tarfile
import tempfile
import re
from pathlib import Path

from models import db, Package, PackageVersion, User, Download
from auth import generate_token, verify_token, hash_password
from storage import StorageBackend, LocalStorage, validate_package_tarball
from search import SearchEngine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'REGISTRY_DB_URL',
    'sqlite:///synapse_registry.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max upload
app.config['SECRET_KEY'] = os.getenv('REGISTRY_SECRET_KEY', 'dev-secret-key')
app.config['STORAGE_PATH'] = os.getenv('REGISTRY_STORAGE_PATH', './packages')

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Initialize extensions
db.init_app(app)
search_engine = SearchEngine()
storage = LocalStorage(app.config['STORAGE_PATH'])

# Ensure storage directory exists
Path(app.config['STORAGE_PATH']).mkdir(parents=True, exist_ok=True)


# ============================================================================
# Helper Functions
# ============================================================================

def require_auth(f):
    """Decorator: Require valid authentication token"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'error': 'Invalid authorization header'}), 401
        
        if not token:
            return jsonify({'error': 'Missing authentication token'}), 401
        
        user_id = verify_token(token)
        if not user_id:
            return jsonify({'error': 'Invalid or expired token'}), 401
        
        request.user_id = user_id
        return f(*args, **kwargs)
    
    return decorated_function


def validate_package_name(name: str) -> bool:
    """Validate package name format: lowercase, alphanumeric, hyphens"""
    pattern = r'^[a-z0-9]([a-z0-9-]{0,214}[a-z0-9])?$'
    return bool(re.match(pattern, name)) and len(name) <= 216


def validate_version(version: str) -> bool:
    """Validate semantic version format: X.Y.Z"""
    pattern = r'^\d+\.\d+\.\d+(-[a-zA-Z0-9]+)?$'
    return bool(re.match(pattern, version))


def serialize_package(pkg: Package) -> Dict:
    """Serialize Package model to JSON"""
    return {
        'id': pkg.id,
        'name': pkg.name,
        'description': pkg.description,
        'author': pkg.author,
        'license': pkg.license,
        'homepage': pkg.homepage,
        'repository': pkg.repository,
        'created_at': pkg.created_at.isoformat(),
        'updated_at': pkg.updated_at.isoformat(),
    }


def serialize_version(pv: PackageVersion, full: bool = False) -> Dict:
    """Serialize PackageVersion model to JSON"""
    data = {
        'version': pv.version,
        'published_at': pv.published_at.isoformat(),
        'downloads': pv.download_count,
        'tarball_url': f'/api/v1/packages/{pv.package.name}/{pv.version}/tarball',
    }
    if full:
        data.update({
            'name': pv.package.name,
            'author': pv.package.author,
            'license': pv.package.license,
            'description': pv.package.description,
            'homepage': pv.package.homepage,
            'dependencies': json.loads(pv.dependencies_json) if pv.dependencies_json else {},
            'keywords': json.loads(pv.keywords_json) if pv.keywords_json else [],
            'checksum': pv.checksum,
            'tarball_size': pv.tarball_size,
        })
    return data


# ============================================================================
# API Routes - Authentication
# ============================================================================

@app.route('/api/v1/auth/register', methods=['POST'])
@limiter.limit("5 per hour")
def register():
    """Register new user account"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400
    
    username = data['username'].lower()
    password = data['password']
    
    # Validate input
    if len(username) < 3 or len(username) > 50:
        return jsonify({'error': 'Username must be 3-50 characters'}), 400
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters'}), 400
    
    # Check if user exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already taken'}), 409
    
    # Create user
    user = User(
        username=username,
        password_hash=hash_password(password),
        email=data.get('email', '')
    )
    db.session.add(user)
    db.session.commit()
    
    logger.info(f"New user registered: {username}")
    
    return jsonify({
        'success': True,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
    }), 201


@app.route('/api/v1/auth/login', methods=['POST'])
@limiter.limit("10 per hour")
def login():
    """Login user and return auth token"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400
    
    username = data['username'].lower()
    password = data['password']
    
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    token = generate_token(user.id)
    
    logger.info(f"User logged in: {username}")
    
    return jsonify({
        'success': True,
        'token': token,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
    }), 200


@app.route('/api/v1/auth/verify', methods=['POST'])
def verify():
    """Verify authentication token"""
    data = request.get_json()
    token = data.get('token') if data else None
    
    if not token:
        return jsonify({'error': 'Missing token'}), 400
    
    user_id = verify_token(token)
    if not user_id:
        return jsonify({'valid': False}), 200
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'valid': False}), 200
    
    return jsonify({
        'valid': True,
        'user': {
            'id': user.id,
            'username': user.username,
        }
    }), 200


# ============================================================================
# API Routes - Package Publishing
# ============================================================================

@app.route('/api/v1/packages', methods=['POST'])
@limiter.limit("10 per hour")
@require_auth
def publish_package():
    """Publish new package version"""
    data = request.get_json()
    
    # Validate required fields
    required = ['name', 'version', 'tarball', 'description']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    name = data['name'].lower()
    version = data['version']
    description = data.get('description', '')
    author = data.get('author', '')
    license = data.get('license', 'MIT')
    homepage = data.get('homepage', '')
    repository = data.get('repository', '')
    keywords = data.get('keywords', [])
    dependencies = data.get('dependencies', {})
    
    # Validate name and version
    if not validate_package_name(name):
        return jsonify({'error': 'Invalid package name format'}), 400
    if not validate_version(version):
        return jsonify({'error': 'Invalid version format (use X.Y.Z)'}), 400
    
    # Decode tarball from base64
    try:
        import base64
        tarball_bytes = base64.b64decode(data['tarball'])
    except Exception as e:
        return jsonify({'error': f'Invalid tarball encoding: {str(e)}'}), 400
    
    # Validate tarball contents
    try:
        validate_package_tarball(tarball_bytes)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    # Check if package exists
    pkg = Package.query.filter_by(name=name).first()
    if not pkg:
        pkg = Package(
            name=name,
            description=description,
            author=author,
            license=license,
            homepage=homepage,
            repository=repository,
            owner_id=request.user_id,
        )
        db.session.add(pkg)
    else:
        # Verify ownership
        if pkg.owner_id != request.user_id:
            return jsonify({'error': 'You do not own this package'}), 403
        # Update metadata
        pkg.description = description
        pkg.author = author
        pkg.license = license
        pkg.homepage = homepage
        pkg.repository = repository
    
    # Check if version already exists
    pv = PackageVersion.query.filter_by(
        package_id=pkg.id,
        version=version
    ).first()
    if pv:
        return jsonify({'error': f'Version {version} already published'}), 409
    
    # Calculate checksum
    checksum = hashlib.sha256(tarball_bytes).hexdigest()
    
    # Store tarball
    storage_path = storage.save_tarball(name, version, tarball_bytes)
    
    # Create package version
    pv = PackageVersion(
        package_id=pkg.id,
        version=version,
        checksum=checksum,
        tarball_path=storage_path,
        tarball_size=len(tarball_bytes),
        keywords_json=json.dumps(keywords),
        dependencies_json=json.dumps(dependencies),
    )
    
    db.session.add(pv)
    db.session.commit()
    
    # Index for search
    search_engine.index_package(pkg, pv)
    
    logger.info(f"Package published: {name}@{version} by user {request.user_id}")
    
    return jsonify({
        'success': True,
        'package': {
            'id': pkg.id,
            'name': pkg.name,
            'version': version,
            'published_at': pv.published_at.isoformat(),
            'url': f'/api/v1/packages/{name}/{version}',
        }
    }), 201


# ============================================================================
# API Routes - Package Discovery
# ============================================================================

@app.route('/api/v1/packages/<name>', methods=['GET'])
@limiter.limit("100 per minute")
def get_package(name: str):
    """Get package metadata and all versions"""
    name = name.lower()
    pkg = Package.query.filter_by(name=name).first()
    
    if not pkg:
        return jsonify({'error': f'Package {name} not found'}), 404
    
    versions = PackageVersion.query.filter_by(
        package_id=pkg.id
    ).order_by(PackageVersion.published_at.desc()).all()
    
    downloads_total = sum(v.download_count for v in versions)
    downloads_week = sum(
        v.download_count for v in versions
        if v.published_at > datetime.utcnow() - timedelta(days=7)
    )
    downloads_month = sum(
        v.download_count for v in versions
        if v.published_at > datetime.utcnow() - timedelta(days=30)
    )
    
    return jsonify({
        'name': pkg.name,
        'description': pkg.description,
        'author': pkg.author,
        'license': pkg.license,
        'homepage': pkg.homepage,
        'repository': pkg.repository,
        'created_at': pkg.created_at.isoformat(),
        'updated_at': pkg.updated_at.isoformat(),
        'versions': [serialize_version(v) for v in versions],
        'downloads': {
            'total': downloads_total,
            'week': downloads_week,
            'month': downloads_month,
        }
    }), 200


@app.route('/api/v1/packages/<name>/<version>', methods=['GET'])
@limiter.limit("100 per minute")
def get_package_version(name: str, version: str):
    """Get specific package version metadata"""
    name = name.lower()
    pkg = Package.query.filter_by(name=name).first()
    
    if not pkg:
        return jsonify({'error': f'Package {name} not found'}), 404
    
    pv = PackageVersion.query.filter_by(
        package_id=pkg.id,
        version=version
    ).first()
    
    if not pv:
        return jsonify({'error': f'Version {version} not found'}), 404
    
    return jsonify(serialize_version(pv, full=True)), 200


@app.route('/api/v1/packages/<name>/<version>/tarball', methods=['GET'])
@limiter.limit("50 per minute")
def download_tarball(name: str, version: str):
    """Download package tarball"""
    name = name.lower()
    pkg = Package.query.filter_by(name=name).first()
    
    if not pkg:
        return jsonify({'error': f'Package {name} not found'}), 404
    
    pv = PackageVersion.query.filter_by(
        package_id=pkg.id,
        version=version
    ).first()
    
    if not pv:
        return jsonify({'error': f'Version {version} not found'}), 404
    
    # Increment download counter
    pv.download_count += 1
    
    # Log download
    download = Download(
        package_version_id=pv.id,
        ip_address=get_remote_address(),
    )
    db.session.add(download)
    db.session.commit()
    
    logger.info(f"Package downloaded: {name}@{version}")
    
    # Send tarball
    try:
        return send_file(
            pv.tarball_path,
            mimetype='application/gzip',
            as_attachment=True,
            download_name=f'{name}-{version}.tar.gz'
        )
    except FileNotFoundError:
        return jsonify({'error': 'Tarball file not found'}), 404


@app.route('/api/v1/packages/<name>/versions', methods=['GET'])
@limiter.limit("100 per minute")
def list_versions(name: str):
    """List all versions of a package"""
    name = name.lower()
    pkg = Package.query.filter_by(name=name).first()
    
    if not pkg:
        return jsonify({'error': f'Package {name} not found'}), 404
    
    versions = PackageVersion.query.filter_by(
        package_id=pkg.id
    ).order_by(PackageVersion.published_at.desc()).all()
    
    return jsonify({
        'name': pkg.name,
        'versions': [v.version for v in versions]
    }), 200


@app.route('/api/v1/search', methods=['GET'])
@limiter.limit("100 per minute")
def search_packages():
    """Search packages by name/keywords/description"""
    query = request.args.get('q', '').strip()
    limit = min(int(request.args.get('limit', 20)), 100)
    offset = int(request.args.get('offset', 0))
    
    if not query:
        return jsonify({'error': 'Missing search query'}), 400
    
    # Search packages
    results, total = search_engine.search(query, limit, offset)
    
    return jsonify({
        'results': results,
        'total': total,
        'limit': limit,
        'offset': offset,
    }), 200


# ============================================================================
# API Routes - Package Management
# ============================================================================

@app.route('/api/v1/packages/<name>/<version>', methods=['DELETE'])
@limiter.limit("20 per hour")
@require_auth
def delete_package_version(name: str, version: str):
    """Delete package version (owner only)"""
    name = name.lower()
    pkg = Package.query.filter_by(name=name).first()
    
    if not pkg:
        return jsonify({'error': f'Package {name} not found'}), 404
    
    if pkg.owner_id != request.user_id:
        return jsonify({'error': 'You do not own this package'}), 403
    
    pv = PackageVersion.query.filter_by(
        package_id=pkg.id,
        version=version
    ).first()
    
    if not pv:
        return jsonify({'error': f'Version {version} not found'}), 404
    
    # Delete tarball from storage
    try:
        storage.delete_tarball(pv.tarball_path)
    except Exception as e:
        logger.error(f"Error deleting tarball: {e}")
    
    # Delete from database
    db.session.delete(pv)
    db.session.commit()
    
    logger.info(f"Package deleted: {name}@{version} by user {request.user_id}")
    
    return '', 204


# ============================================================================
# API Routes - Statistics
# ============================================================================

@app.route('/api/v1/stats', methods=['GET'])
@limiter.limit("100 per minute")
def get_stats():
    """Get registry statistics"""
    total_packages = Package.query.count()
    total_versions = PackageVersion.query.count()
    total_downloads = db.session.query(
        db.func.sum(PackageVersion.download_count)
    ).scalar() or 0
    
    # Top packages
    top_packages = db.session.query(
        Package.name,
        db.func.sum(PackageVersion.download_count).label('downloads')
    ).join(PackageVersion).group_by(Package.id).order_by(
        db.desc('downloads')
    ).limit(10).all()
    
    return jsonify({
        'timestamp': datetime.utcnow().isoformat(),
        'packages': {
            'total': total_packages,
            'versions': total_versions,
            'downloads': int(total_downloads),
        },
        'top_packages': [
            {'name': name, 'downloads': downloads}
            for name, downloads in top_packages
        ]
    }), 200


# ============================================================================
# Health & Status
# ============================================================================

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
    }), 200


# ============================================================================
# Error Handlers
# ============================================================================

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500


# ============================================================================
# Initialization
# ============================================================================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        logger.info("Database initialized")
    
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('REGISTRY_PORT', 8080)),
        debug=debug
    )
