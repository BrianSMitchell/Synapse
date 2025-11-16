"""Publish Command - Upload packages to registry

Handles:
- Package preparation and validation
- Tarball creation
- Registry upload with progress tracking
- Version conflict handling
"""

import os
import json
import tarfile
import hashlib
import tempfile
from pathlib import Path
from typing import Optional, Dict, Any
import argparse
import requests
from .config import CLIConfig
from .auth import AuthManager
from .utils import ProgressBar, print_success, print_error, print_warning


class PublishCommand:
    """Handles package publishing."""
    
    def __init__(self, config: CLIConfig, auth_manager: AuthManager):
        """Initialize publish command.
        
        Args:
            config: CLI configuration
            auth_manager: Authentication manager
        """
        self.config = config
        self.auth_manager = auth_manager
    
    def execute(self, args: argparse.Namespace) -> int:
        """Execute publish command.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code (0 = success, non-zero = error)
        """
        package_path = Path(args.package)
        
        # Validate package
        if not package_path.exists():
            print_error(f"Package not found: {package_path}")
            return 1
        
        # Check authentication
        if not self.auth_manager.is_authenticated():
            print_error("Not authenticated. Please run 'synapse pkg login' first")
            return 1
        
        try:
            # Load manifest
            manifest = self._load_manifest(package_path)
            if not manifest:
                return 1
            
            # Validate manifest
            if not self._validate_manifest(manifest):
                return 1
            
            # Create tarball
            print("Creating package tarball...")
            tarball_path = self._create_tarball(package_path, manifest)
            
            # Calculate checksum
            checksum = self._calculate_checksum(tarball_path)
            
            # Publish to registry
            print(f"Publishing {manifest['name']} v{manifest['version']}...")
            success = self._publish_to_registry(tarball_path, manifest, checksum, args.force)
            
            # Cleanup
            tarball_path.unlink()
            
            if success:
                print_success(
                    f"✓ Published {manifest['name']} v{manifest['version']} to {self.config.registry_url}"
                )
                return 0
            else:
                return 1
        
        except Exception as e:
            print_error(f"Publish failed: {e}")
            return 1
    
    def _load_manifest(self, package_path: Path) -> Optional[Dict[str, Any]]:
        """Load package manifest.
        
        Args:
            package_path: Path to package directory
            
        Returns:
            Manifest dictionary or None if error
        """
        manifest_file = package_path / 'synapse.json'
        
        if not manifest_file.exists():
            print_error(f"No synapse.json found in {package_path}")
            return None
        
        try:
            with open(manifest_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print_error(f"Invalid synapse.json: {e}")
            return None
    
    def _validate_manifest(self, manifest: Dict[str, Any]) -> bool:
        """Validate package manifest.
        
        Args:
            manifest: Manifest to validate
            
        Returns:
            True if valid, False otherwise
        """
        required_fields = ['name', 'version', 'description', 'author']
        
        for field in required_fields:
            if field not in manifest:
                print_error(f"Missing required field in synapse.json: {field}")
                return False
        
        name = manifest['name']
        if not self._is_valid_package_name(name):
            print_error(f"Invalid package name: {name}")
            return False
        
        version = manifest['version']
        if not self._is_valid_version(version):
            print_error(f"Invalid version: {version}")
            return False
        
        return True
    
    @staticmethod
    def _is_valid_package_name(name: str) -> bool:
        """Validate package name.
        
        Args:
            name: Package name
            
        Returns:
            True if valid
        """
        import re
        # Must be lowercase alphanumeric with hyphens/underscores
        return bool(re.match(r'^[a-z0-9_-]{1,64}$', name))
    
    @staticmethod
    def _is_valid_version(version: str) -> bool:
        """Validate semantic version.
        
        Args:
            version: Version string
            
        Returns:
            True if valid
        """
        import re
        # Semver: MAJOR.MINOR.PATCH[-prerelease][+build]
        return bool(re.match(
            r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?(\+[a-zA-Z0-9.-]+)?$',
            version
        ))
    
    def _create_tarball(self, package_path: Path, manifest: Dict[str, Any]) -> Path:
        """Create package tarball.
        
        Args:
            package_path: Path to package directory
            manifest: Package manifest
            
        Returns:
            Path to created tarball
        """
        name = manifest['name']
        version = manifest['version']
        tarball_name = f"{name}-{version}.tar.gz"
        tarball_path = Path(tempfile.gettempdir()) / tarball_name
        
        # Files to include
        include_patterns = ['*.syn', '*.json', '*.md', 'lib/', 'src/']
        exclude_patterns = ['node_modules/', '.git/', '__pycache__/', '.pytest_cache/']
        
        with tarfile.open(tarball_path, 'w:gz') as tar:
            for item in package_path.rglob('*'):
                if item.is_file():
                    rel_path = item.relative_to(package_path)
                    
                    # Check include patterns
                    include = False
                    for pattern in include_patterns:
                        if '*' in pattern:
                            if item.suffix == pattern.replace('*', ''):
                                include = True
                                break
                        elif str(rel_path).startswith(pattern):
                            include = True
                            break
                    
                    # Check exclude patterns
                    exclude = False
                    for pattern in exclude_patterns:
                        if str(rel_path).startswith(pattern):
                            exclude = True
                            break
                    
                    if include and not exclude:
                        tar.add(item, arcname=f"{name}-{version}/{rel_path}")
        
        return tarball_path
    
    @staticmethod
    def _calculate_checksum(file_path: Path) -> str:
        """Calculate SHA256 checksum of file.
        
        Args:
            file_path: Path to file
            
        Returns:
            Hex checksum
        """
        sha256 = hashlib.sha256()
        
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        
        return sha256.hexdigest()
    
    def _publish_to_registry(self, tarball_path: Path, manifest: Dict[str, Any],
                            checksum: str, force: bool = False) -> bool:
        """Upload package to registry.
        
        Args:
            tarball_path: Path to tarball
            manifest: Package manifest
            checksum: SHA256 checksum
            force: Force publish even if version exists
            
        Returns:
            True if successful
        """
        token = self.auth_manager.get_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'X-Checksum-SHA256': checksum
        }
        
        if force:
            headers['X-Force'] = 'true'
        
        try:
            with open(tarball_path, 'rb') as f:
                files = {
                    'tarball': f,
                    'metadata': (None, json.dumps(manifest), 'application/json')
                }
                
                response = requests.post(
                    f"{self.config.registry_url}/api/v1/packages",
                    files=files,
                    headers=headers,
                    timeout=self.config.download_timeout_seconds
                )
            
            if response.status_code == 201:
                return True
            elif response.status_code == 409:
                print_warning("Package version already exists. Use --force to override")
                return False
            elif response.status_code == 401:
                print_error("Authentication failed. Please login again")
                return False
            else:
                try:
                    error_data = response.json()
                    print_error(f"Upload failed: {error_data.get('error', 'Unknown error')}")
                except:
                    print_error(f"Upload failed: {response.status_code}")
                return False
        
        except requests.RequestException as e:
            print_error(f"Network error: {e}")
            return False
