"""Tests for Dependency Resolution

Test coverage:
- Semantic version parsing and comparison
- Version range matching
- Dependency resolution
- Conflict detection
"""

import pytest
from unittest.mock import Mock, patch
from synapse.cli.resolver import SemanticVersion, DependencyResolver
from synapse.cli.config import CLIConfig


class TestSemanticVersion:
    """Test semantic version parsing and comparison."""
    
    def test_parse_simple_version(self):
        """Test parsing simple semantic version."""
        v = SemanticVersion('1.2.3')
        
        assert v.major == 1
        assert v.minor == 2
        assert v.patch == 3
        assert v.prerelease is None
        assert v.build is None
    
    def test_parse_prerelease_version(self):
        """Test parsing prerelease version."""
        v = SemanticVersion('1.2.3-beta.1')
        
        assert v.major == 1
        assert v.minor == 2
        assert v.patch == 3
        assert v.prerelease == 'beta.1'
    
    def test_parse_build_metadata(self):
        """Test parsing build metadata."""
        v = SemanticVersion('1.2.3+build.123')
        
        assert v.major == 1
        assert v.minor == 2
        assert v.patch == 3
        assert v.build == 'build.123'
    
    def test_parse_full_version(self):
        """Test parsing complete version string."""
        v = SemanticVersion('1.2.3-rc.1+build.456')
        
        assert v.major == 1
        assert v.minor == 2
        assert v.patch == 3
        assert v.prerelease == 'rc.1'
        assert v.build == 'build.456'
    
    def test_version_equality(self):
        """Test version equality comparison."""
        v1 = SemanticVersion('1.2.3')
        v2 = SemanticVersion('1.2.3')
        v3 = SemanticVersion('1.2.4')
        
        assert v1 == v2
        assert not (v1 == v3)
        assert v1 == '1.2.3'
    
    def test_version_less_than(self):
        """Test less than comparison."""
        v1 = SemanticVersion('1.2.3')
        v2 = SemanticVersion('1.2.4')
        v3 = SemanticVersion('2.0.0')
        
        assert v1 < v2
        assert v1 < v3
        assert v2 < v3
        assert not (v2 < v1)
    
    def test_prerelease_less_than_release(self):
        """Test that prerelease is less than release."""
        v1 = SemanticVersion('1.2.3-beta')
        v2 = SemanticVersion('1.2.3')
        
        assert v1 < v2
        assert not (v2 < v1)
    
    def test_version_greater_than(self):
        """Test greater than comparison."""
        v1 = SemanticVersion('2.0.0')
        v2 = SemanticVersion('1.2.3')
        
        assert v1 > v2
        assert not (v2 > v1)
    
    def test_version_string_representation(self):
        """Test string representation."""
        v = SemanticVersion('1.2.3-beta.1')
        assert str(v) == '1.2.3-beta.1'
    
    def test_match_exact_version(self):
        """Test matching exact version."""
        v = SemanticVersion('1.2.3')
        
        assert v.matches_range('1.2.3')
        assert not v.matches_range('1.2.4')
    
    def test_match_caret_range(self):
        """Test matching caret range (^1.2.3)."""
        v = SemanticVersion('1.2.5')
        
        assert v.matches_range('^1.2.3')
        assert v.matches_range('^1.0.0')
        assert not v.matches_range('^2.0.0')
    
    def test_match_tilde_range(self):
        """Test matching tilde range (~1.2.3)."""
        v = SemanticVersion('1.2.5')
        
        assert v.matches_range('~1.2.3')
        assert v.matches_range('~1.2.0')
        assert not v.matches_range('~1.3.0')
    
    def test_match_greater_than(self):
        """Test matching greater than."""
        v = SemanticVersion('1.2.4')
        
        assert v.matches_range('>=1.2.3')
        assert v.matches_range('>1.2.3')
        assert not v.matches_range('>=1.2.5')
    
    def test_match_less_than(self):
        """Test matching less than."""
        v = SemanticVersion('1.2.2')
        
        assert v.matches_range('<=1.2.3')
        assert v.matches_range('<1.2.3')
        assert not v.matches_range('<=1.2.1')


class TestDependencyResolver:
    """Test dependency resolution."""
    
    @patch('requests.get')
    def test_resolve_version_exact(self, mock_get):
        """Test resolving exact version."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'versions': ['1.2.3', '1.2.2', '1.2.1']
        }
        mock_get.return_value = mock_response
        
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        version = resolver.resolve_version('mylib', '1.2.3')
        assert version == '1.2.3'
    
    @patch('requests.get')
    def test_resolve_version_latest(self, mock_get):
        """Test resolving to latest version."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'versions': ['2.0.0', '1.5.0', '1.4.0']
        }
        mock_get.return_value = mock_response
        
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        version = resolver.resolve_version('mylib')
        assert version == '2.0.0'
    
    @patch('requests.get')
    def test_resolve_version_range(self, mock_get):
        """Test resolving version from range."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'versions': ['2.0.0', '1.5.3', '1.5.2', '1.5.1', '1.0.0']
        }
        mock_get.return_value = mock_response
        
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        version = resolver.resolve_version('mylib', '^1.5.0')
        assert version in ['1.5.3', '1.5.2', '1.5.1']
    
    @patch('requests.get')
    def test_resolve_version_not_found(self, mock_get):
        """Test when version cannot be resolved."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        version = resolver.resolve_version('nonexistent', '1.0.0')
        assert version is None
    
    @patch('requests.get')
    def test_get_available_versions(self, mock_get):
        """Test getting available versions."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'versions': ['1.2.3', '1.2.2', '1.2.1']
        }
        mock_get.return_value = mock_response
        
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        versions = resolver._get_available_versions('mylib')
        assert len(versions) == 3
        assert versions[0] == '1.2.3'  # Should be sorted descending
    
    @patch('requests.get')
    def test_resolve_dependencies(self, mock_get):
        """Test resolving all dependencies recursively."""
        def mock_get_side_effect(url, **kwargs):
            response = Mock()
            
            if 'versions' in url:
                response.status_code = 200
                response.json.return_value = {'versions': ['1.0.0']}
            elif 'packages/mylib/1.0.0' in url:
                response.status_code = 200
                response.json.return_value = {
                    'dependencies': {'dep1': '1.0.0'}
                }
            elif 'packages/dep1' in url:
                response.status_code = 200
                response.json.return_value = {
                    'dependencies': {}
                }
            else:
                response.status_code = 404
            
            return response
        
        mock_get.side_effect = mock_get_side_effect
        
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        deps = resolver.resolve_dependencies('mylib', '1.0.0')
        assert 'dep1' in deps
    
    def test_detect_conflicts(self):
        """Test detecting version conflicts."""
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        deps = {
            'pkg1': {'shared': '1.0.0'},
            'pkg2': {'shared': '2.0.0'}
        }
        
        conflicts = resolver.detect_conflicts(deps)
        assert len(conflicts) > 0
        assert conflicts[0][0] == 'shared'
    
    def test_no_conflicts(self):
        """Test when there are no conflicts."""
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        deps = {
            'pkg1': {'shared': '1.0.0'},
            'pkg2': {'shared': '1.0.0'}
        }
        
        conflicts = resolver.detect_conflicts(deps)
        assert len(conflicts) == 0
    
    @patch('requests.get')
    def test_version_cache(self, mock_get):
        """Test version caching."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'versions': ['1.0.0']
        }
        mock_get.return_value = mock_response
        
        config = CLIConfig()
        resolver = DependencyResolver(config)
        
        # First call
        resolver._get_available_versions('mylib')
        
        # Second call should use cache
        resolver._get_available_versions('mylib')
        
        # Should only be called once due to caching
        assert mock_get.call_count == 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
