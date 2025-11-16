"""CLI Configuration Management

Handles:
- Registry configuration
- Local cache management
- Authentication storage
- User preferences
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field, asdict


@dataclass
class CLIConfig:
    """Configuration for the Synapse CLI."""
    
    # Registry configuration
    registry_url: str = field(default_factory=lambda: os.environ.get(
        'SYNAPSE_REGISTRY', 'https://registry.synapse.sh'
    ))
    
    # Local paths
    cache_dir: Path = field(default_factory=lambda: Path.home() / '.synapse' / 'cache')
    config_file: Path = field(default_factory=lambda: Path.home() / '.synapse' / 'config.json')
    credentials_file: Path = field(default_factory=lambda: Path.home() / '.synapse' / 'credentials.json')
    packages_dir: Path = field(default_factory=lambda: Path.home() / '.synapse' / 'packages')
    lock_file: Path = field(default_factory=lambda: Path('.') / 'synapse-lock.json')
    manifest_file: Path = field(default_factory=lambda: Path('.') / 'synapse.json')
    
    # Cache settings
    cache_enabled: bool = True
    cache_ttl_hours: int = 24
    
    # Performance settings
    max_retries: int = 3
    retry_delay_seconds: float = 1.0
    connection_timeout_seconds: float = 30.0
    download_timeout_seconds: float = 300.0
    
    # UI settings
    show_progress_bars: bool = True
    colorize_output: bool = True
    
    # Storage settings
    max_cache_size_mb: int = 500
    
    def __post_init__(self):
        """Initialize configuration after creation."""
        self._ensure_directories()
        self._load_config()
    
    def _ensure_directories(self) -> None:
        """Ensure all required directories exist."""
        for directory in [self.cache_dir, self.packages_dir]:
            directory.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> None:
        """Load configuration from file if it exists."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config_data = json.load(f)
                    
                    # Update fields from config file
                    for key, value in config_data.items():
                        if hasattr(self, key):
                            if key in ['cache_dir', 'packages_dir', 'lock_file', 'manifest_file']:
                                setattr(self, key, Path(value))
                            else:
                                setattr(self, key, value)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load config: {e}")
    
    def save_config(self) -> None:
        """Save configuration to file."""
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        
        config_data = asdict(self)
        # Convert Path objects to strings for JSON serialization
        for key in ['cache_dir', 'config_file', 'credentials_file', 'packages_dir', 'lock_file', 'manifest_file']:
            if key in config_data:
                config_data[key] = str(config_data[key])
        
        with open(self.config_file, 'w') as f:
            json.dump(config_data, f, indent=2)
    
    def get_cache_path(self, key: str) -> Path:
        """Get cache file path for a key.
        
        Args:
            key: Cache key (e.g., 'package_mylib')
            
        Returns:
            Path to cache file
        """
        return self.cache_dir / f"{key}.json"
    
    def clear_cache(self) -> None:
        """Clear all cached files."""
        if self.cache_dir.exists():
            import shutil
            shutil.rmtree(self.cache_dir)
            self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def get_cache_size_mb(self) -> float:
        """Get total size of cache directory in MB.
        
        Returns:
            Cache size in megabytes
        """
        total_size = 0
        if self.cache_dir.exists():
            for file in self.cache_dir.rglob('*'):
                if file.is_file():
                    total_size += file.stat().st_size
        return total_size / (1024 * 1024)
    
    def is_cache_expired(self, cache_file: Path) -> bool:
        """Check if cache file is expired.
        
        Args:
            cache_file: Path to cache file
            
        Returns:
            True if expired, False otherwise
        """
        if not cache_file.exists():
            return True
        
        import time
        mtime = cache_file.stat().st_mtime
        age_hours = (time.time() - mtime) / 3600
        
        return age_hours > self.cache_ttl_hours


class CredentialsManager:
    """Manages stored credentials."""
    
    def __init__(self, config: CLIConfig):
        """Initialize credentials manager.
        
        Args:
            config: CLI configuration
        """
        self.config = config
        self._credentials: Dict[str, Dict[str, Any]] = {}
        self._load_credentials()
    
    def _load_credentials(self) -> None:
        """Load credentials from file."""
        if self.config.credentials_file.exists():
            try:
                with open(self.config.credentials_file, 'r') as f:
                    self._credentials = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._credentials = {}
    
    def _save_credentials(self) -> None:
        """Save credentials to file."""
        self.config.credentials_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Set restrictive permissions
        with open(self.config.credentials_file, 'w') as f:
            json.dump(self._credentials, f, indent=2)
        
        # chmod 600 (read/write owner only)
        os.chmod(self.config.credentials_file, 0o600)
    
    def store_token(self, registry: str, token: str, username: str = '') -> None:
        """Store authentication token.
        
        Args:
            registry: Registry URL
            token: Authentication token
            username: Username (optional)
        """
        if registry not in self._credentials:
            self._credentials[registry] = {}
        
        self._credentials[registry]['token'] = token
        if username:
            self._credentials[registry]['username'] = username
        
        self._save_credentials()
    
    def get_token(self, registry: str) -> Optional[str]:
        """Get stored token for registry.
        
        Args:
            registry: Registry URL
            
        Returns:
            Token if found, None otherwise
        """
        if registry in self._credentials:
            return self._credentials[registry].get('token')
        return None
    
    def delete_token(self, registry: str) -> bool:
        """Delete stored token.
        
        Args:
            registry: Registry URL
            
        Returns:
            True if deleted, False if not found
        """
        if registry in self._credentials:
            del self._credentials[registry]
            self._save_credentials()
            return True
        return False
    
    def clear_all(self) -> None:
        """Clear all stored credentials."""
        self._credentials = {}
        self._save_credentials()
    
    def list_registries(self) -> list:
        """List all configured registries.
        
        Returns:
            List of registry URLs
        """
        return list(self._credentials.keys())
