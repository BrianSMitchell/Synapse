"""Tests for Synapse CLI Core Module

Test coverage:
- Argument parsing
- Command routing
- Configuration management
- Credentials handling
"""

import pytest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from synapse.cli.cli import SynapseCLI
from synapse.cli.config import CLIConfig, CredentialsManager
from synapse.cli.auth import AuthManager


class TestCLIArgumentParsing:
    """Test argument parsing and command routing."""
    
    def test_parse_publish_command(self):
        """Test parsing publish command."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['publish', './mylib'])
        
        assert args.command == 'publish'
        assert args.package == './mylib'
    
    def test_parse_install_command(self):
        """Test parsing install command."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['install', 'mylib', 'other@1.0.0'])
        
        assert args.command == 'install'
        assert args.packages == ['mylib', 'other@1.0.0']
    
    def test_parse_install_with_save(self):
        """Test parsing install with --save flag."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['install', 'mylib', '--save'])
        
        assert args.command == 'install'
        assert getattr(args, 'save', False) is True
    
    def test_parse_search_command(self):
        """Test parsing search command."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['search', 'machine-learning', '--limit', '20'])
        
        assert args.command == 'search'
        assert args.query == 'machine-learning'
        assert args.limit == 20
    
    def test_parse_info_command(self):
        """Test parsing info command."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['info', 'mylib', '--version', '1.2.3'])
        
        assert args.command == 'info'
        assert args.package == 'mylib'
        assert args.version == '1.2.3'
    
    def test_parse_list_command(self):
        """Test parsing list command."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['list', '--global', '--depth', '2'])
        
        assert args.command == 'list'
        assert getattr(args, 'global') is True
        assert args.depth == 2
    
    def test_parse_login_command(self):
        """Test parsing login command."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['login', '-u', 'user'])
        
        assert args.command == 'login'
        assert args.username == 'user'
    
    def test_parse_update_command(self):
        """Test parsing update command."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['update', 'mylib'])
        
        assert args.command == 'update'
        assert args.packages == ['mylib']
    
    def test_version_flag(self):
        """Test --version flag."""
        cli = SynapseCLI()
        parser = cli.create_parser()
        
        with pytest.raises(SystemExit):
            parser.parse_args(['--version'])
    
    def test_verbose_flag(self):
        """Test --verbose flag."""
        cli = SynapseCLI()
        args = cli.create_parser().parse_args(['--verbose', 'list'])
        
        assert args.verbose is True


class TestCLIConfig:
    """Test CLI configuration."""
    
    def test_config_initialization(self):
        """Test config initialization with defaults."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            
            assert config.registry_url == 'https://registry.synapse.sh'
            assert config.cache_ttl_hours == 24
            assert config.max_retries == 3
    
    def test_config_directories_creation(self):
        """Test that required directories are created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            
            assert config.cache_dir.exists()
            assert config.packages_dir.exists()
    
    def test_config_save_and_load(self):
        """Test saving and loading configuration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.config_file = Path(tmpdir) / 'config.json'
            config.cache_ttl_hours = 12
            
            config.save_config()
            
            assert config.config_file.exists()
            
            # Load in new instance
            config2 = CLIConfig()
            config2.config_file = config.config_file
            config2._load_config()
            
            assert config2.cache_ttl_hours == 12
    
    def test_get_cache_path(self):
        """Test getting cache file path."""
        config = CLIConfig()
        cache_path = config.get_cache_path('test_key')
        
        assert cache_path.name == 'test_key.json'
        assert 'cache' in str(cache_path)
    
    def test_cache_size_calculation(self):
        """Test cache size calculation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.cache_dir = Path(tmpdir) / 'cache'
            config.cache_dir.mkdir(parents=True)
            
            # Create test cache file
            test_file = config.cache_dir / 'test.json'
            test_file.write_bytes(b'x' * 1024)  # 1 KB
            
            size_mb = config.get_cache_size_mb()
            assert size_mb > 0
    
    def test_cache_expiration(self):
        """Test cache expiration checking."""
        import time
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.cache_dir = Path(tmpdir) / 'cache'
            config.cache_dir.mkdir(parents=True)
            config.cache_ttl_hours = 0  # Immediate expiration
            
            test_file = config.cache_dir / 'test.json'
            test_file.write_text('{}')
            
            time.sleep(0.1)
            assert config.is_cache_expired(test_file)
    
    def test_clear_cache(self):
        """Test clearing cache."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.cache_dir = Path(tmpdir) / 'cache'
            config.cache_dir.mkdir(parents=True)
            
            # Create test file
            test_file = config.cache_dir / 'test.json'
            test_file.write_text('{}')
            
            assert test_file.exists()
            config.clear_cache()
            assert not test_file.exists()


class TestCredentialsManager:
    """Test credential storage and management."""
    
    def test_store_and_retrieve_token(self):
        """Test storing and retrieving authentication token."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            manager = CredentialsManager(config)
            manager.store_token('https://registry.example.com', 'test_token', 'testuser')
            
            token = manager.get_token('https://registry.example.com')
            assert token == 'test_token'
    
    def test_delete_token(self):
        """Test deleting stored token."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            manager = CredentialsManager(config)
            manager.store_token('https://registry.example.com', 'test_token')
            
            success = manager.delete_token('https://registry.example.com')
            assert success is True
            
            token = manager.get_token('https://registry.example.com')
            assert token is None
    
    def test_list_registries(self):
        """Test listing configured registries."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            manager = CredentialsManager(config)
            manager.store_token('https://registry1.example.com', 'token1')
            manager.store_token('https://registry2.example.com', 'token2')
            
            registries = manager.list_registries()
            assert len(registries) == 2
    
    def test_clear_all_credentials(self):
        """Test clearing all credentials."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            manager = CredentialsManager(config)
            manager.store_token('https://registry1.example.com', 'token1')
            manager.store_token('https://registry2.example.com', 'token2')
            
            manager.clear_all()
            
            registries = manager.list_registries()
            assert len(registries) == 0


class TestAuthManager:
    """Test authentication manager."""
    
    @patch('requests.post')
    def test_login_success(self, mock_post):
        """Test successful login."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'token': 'test_token'}
        mock_post.return_value = mock_response
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            auth = AuthManager(config)
            success = auth.login('testuser', 'testpass')
            
            assert success is True
            mock_post.assert_called_once()
    
    @patch('requests.post')
    def test_login_failure(self, mock_post):
        """Test failed login."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_post.return_value = mock_response
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            auth = AuthManager(config)
            success = auth.login('testuser', 'wrongpass')
            
            assert success is False
    
    def test_get_token(self):
        """Test getting stored token."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            auth = AuthManager(config)
            auth.credentials.store_token(config.registry_url, 'test_token')
            
            token = auth.get_token()
            assert token == 'test_token'
    
    def test_is_authenticated(self):
        """Test authentication check."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            auth = AuthManager(config)
            
            assert not auth.is_authenticated()
            
            auth.credentials.store_token(config.registry_url, 'test_token')
            assert auth.is_authenticated()
    
    @patch('requests.post')
    def test_verify_token(self, mock_post):
        """Test token verification."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            auth = AuthManager(config)
            auth.credentials.store_token(config.registry_url, 'test_token')
            
            valid = auth.verify_token()
            assert valid is True
    
    def test_get_headers_with_token(self):
        """Test getting HTTP headers with authentication."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = CLIConfig()
            config.credentials_file = Path(tmpdir) / 'creds.json'
            
            auth = AuthManager(config)
            auth.credentials.store_token(config.registry_url, 'test_token')
            
            headers = auth.get_headers()
            assert 'Authorization' in headers
            assert headers['Authorization'] == 'Bearer test_token'


class TestCLIRunMethod:
    """Test CLI run method."""
    
    def test_run_with_no_command(self):
        """Test running with no command."""
        cli = SynapseCLI()
        
        with patch('sys.stdout'):
            exit_code = cli.run([])
        
        assert exit_code == 0
    
    def test_run_with_unknown_command(self):
        """Test running with unknown command."""
        cli = SynapseCLI()
        
        # argparse exits with code 2 for invalid commands
        with pytest.raises(SystemExit) as exc_info:
            cli.run(['unknown'])
        
        assert exc_info.value.code == 2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
