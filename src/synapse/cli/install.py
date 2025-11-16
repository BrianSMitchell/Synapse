"""Install Command - Download and install packages

Handles:
- Package resolution
- Dependency resolution
- Download management
- Installation to local directory
- Lock file generation
"""

import json
import tarfile
import tempfile
from pathlib import Path
from typing import Optional, Dict, Any, List, Set
import argparse
import requests
from .config import CLIConfig
from .auth import AuthManager
from .resolver import DependencyResolver
from .utils import ProgressBar, print_success, print_error, print_warning


class InstallCommand:
    """Handles package installation."""
    
    def __init__(self, config: CLIConfig, auth_manager: AuthManager):
        """Initialize install command.
        
        Args:
            config: CLI configuration
            auth_manager: Authentication manager
        """
        self.config = config
        self.auth_manager = auth_manager
        self.resolver = DependencyResolver(config)
    
    def execute(self, args: argparse.Namespace) -> int:
        """Execute install command.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code (0 = success, non-zero = error)
        """
        try:
            # Determine install mode
            if args.command == 'update':
                # Update mode: update existing packages
                return self._update_packages(args)
            else:
                # Install mode: install new packages or dependencies
                return self._install_packages(args)
        
        except Exception as e:
            print_error(f"Installation failed: {e}")
            return 1
    
    def _install_packages(self, args: argparse.Namespace) -> int:
        """Install packages.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code
        """
        packages = args.packages if args.packages else []
        
        if not packages:
            # No packages specified - install from synapse.json
            return self._install_from_manifest()
        
        # Install specified packages
        print(f"Installing {len(packages)} package(s)...")
        
        installed = []
        failed = []
        
        for package_spec in packages:
            # Parse package@version
            if '@' in package_spec:
                name, version = package_spec.split('@', 1)
            else:
                name = package_spec
                version = None
            
            if self._install_package(name, version, args):
                installed.append(package_spec)
            else:
                failed.append(package_spec)
        
        # Summary
        print()
        if installed:
            print_success(f"✓ Installed {len(installed)} package(s)")
        
        if failed:
            print_error(f"✗ Failed to install {len(failed)} package(s)")
            for pkg in failed:
                print_error(f"  - {pkg}")
        
        return 0 if not failed else 1
    
    def _install_from_manifest(self) -> int:
        """Install packages from synapse.json.
        
        Returns:
            Exit code
        """
        manifest_file = self.config.manifest_file
        
        if not manifest_file.exists():
            print_error("No synapse.json found in current directory")
            return 1
        
        try:
            with open(manifest_file, 'r') as f:
                manifest = json.load(f)
        except json.JSONDecodeError as e:
            print_error(f"Invalid synapse.json: {e}")
            return 1
        
        # Get dependencies
        dependencies = manifest.get('dependencies', {})
        dev_dependencies = manifest.get('devDependencies', {})
        
        all_deps = {**dependencies, **dev_dependencies}
        
        if not all_deps:
            print("No dependencies to install")
            return 0
        
        print(f"Installing {len(all_deps)} dependencies...")
        
        failed = []
        for name, version_spec in all_deps.items():
            if not self._install_package(name, version_spec, None):
                failed.append(name)
        
        if failed:
            print_error(f"Failed to install: {', '.join(failed)}")
            return 1
        
        # Generate lock file
        self._generate_lock_file(all_deps)
        
        print_success("✓ Dependencies installed successfully")
        return 0
    
    def _install_package(self, name: str, version: Optional[str], args: Any) -> bool:
        """Install a single package.
        
        Args:
            name: Package name
            version: Version spec (or None for latest)
            args: Command arguments
            
        Returns:
            True if successful
        """
        print(f"  Installing {name}@{version or 'latest'}...", end=' ')
        
        # Resolve version
        resolved_version = self.resolver.resolve_version(name, version)
        if not resolved_version:
            print_error(f"Could not resolve version for {name}")
            return False
        
        # Download package
        if not self._download_package(name, resolved_version):
            print_error(f"Failed to download {name}")
            return False
        
        # Install package
        install_dir = self.config.packages_dir / name / resolved_version
        if not self._extract_package(name, resolved_version, install_dir):
            print_error(f"Failed to extract {name}")
            return False
        
        print_success(f"✓ {resolved_version}")
        return True
    
    def _update_packages(self, args: argparse.Namespace) -> int:
        """Update packages.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code
        """
        packages = args.packages if args.packages else []
        
        if not packages:
            # Update all from synapse.json
            manifest_file = self.config.manifest_file
            if not manifest_file.exists():
                print_error("No synapse.json found")
                return 1
            
            try:
                with open(manifest_file, 'r') as f:
                    manifest = json.load(f)
                    packages = list(manifest.get('dependencies', {}).keys())
            except json.JSONDecodeError as e:
                print_error(f"Invalid synapse.json: {e}")
                return 1
        
        print(f"Updating {len(packages)} package(s)...")
        
        updated = []
        failed = []
        
        for package_name in packages:
            if self._install_package(package_name, None, None):
                updated.append(package_name)
            else:
                failed.append(package_name)
        
        print()
        if updated:
            print_success(f"✓ Updated {len(updated)} package(s)")
        
        if failed:
            print_error(f"✗ Failed to update {len(failed)} package(s)")
        
        return 0 if not failed else 1
    
    def _download_package(self, name: str, version: str) -> bool:
        """Download package tarball.
        
        Args:
            name: Package name
            version: Package version
            
        Returns:
            True if successful
        """
        cache_file = self.config.get_cache_path(f"{name}-{version}")
        
        # Check cache
        if cache_file.exists() and not self.config.is_cache_expired(cache_file):
            return True
        
        try:
            url = f"{self.config.registry_url}/api/v1/packages/{name}/{version}/tarball"
            
            response = requests.get(
                url,
                timeout=self.config.download_timeout_seconds,
                stream=True
            )
            
            if response.status_code != 200:
                return False
            
            # Save to cache
            cache_file.parent.mkdir(parents=True, exist_ok=True)
            with open(cache_file, 'wb') as f:
                for chunk in response.iter_content(8192):
                    f.write(chunk)
            
            return True
        
        except requests.RequestException:
            return False
    
    def _extract_package(self, name: str, version: str, install_dir: Path) -> bool:
        """Extract package from cache.
        
        Args:
            name: Package name
            version: Package version
            install_dir: Installation directory
            
        Returns:
            True if successful
        """
        cache_file = self.config.get_cache_path(f"{name}-{version}")
        
        if not cache_file.exists():
            return False
        
        try:
            install_dir.mkdir(parents=True, exist_ok=True)
            
            with tarfile.open(cache_file, 'r:gz') as tar:
                tar.extractall(path=install_dir)
            
            return True
        
        except (tarfile.TarError, IOError):
            return False
    
    def _generate_lock_file(self, dependencies: Dict[str, str]) -> None:
        """Generate lock file with exact versions.
        
        Args:
            dependencies: Dependency dictionary
        """
        lock_data = {
            'dependencies': {},
            'version': '1.0'
        }
        
        for name, version_spec in dependencies.items():
            resolved = self.resolver.resolve_version(name, version_spec)
            if resolved:
                lock_data['dependencies'][name] = resolved
        
        with open(self.config.lock_file, 'w') as f:
            json.dump(lock_data, f, indent=2)
