"""Info Command - Show package information

Handles:
- Fetching package metadata
- Displaying detailed information
- Version history
"""

import json
import requests
from typing import Dict, Any, Optional
import argparse
from .config import CLIConfig
from .utils import print_error


class InfoCommand:
    """Handles package info display."""
    
    def __init__(self, config: CLIConfig):
        """Initialize info command.
        
        Args:
            config: CLI configuration
        """
        self.config = config
    
    def execute(self, args: argparse.Namespace) -> int:
        """Execute info command.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code
        """
        name = args.package
        version = getattr(args, 'version', None)
        
        try:
            pkg_info = self._get_package_info(name, version)
            
            if not pkg_info:
                print_error(f"Package not found: {name}")
                return 1
            
            self._display_info(pkg_info)
            return 0
        
        except Exception as e:
            print_error(f"Failed to get package info: {e}")
            return 1
    
    def _get_package_info(self, name: str, version: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Get package information from registry.
        
        Args:
            name: Package name
            version: Specific version (or None for latest)
            
        Returns:
            Package info dictionary or None
        """
        # Check cache
        cache_key = f"info_{name}_{version or 'latest'}"
        cache_file = self.config.get_cache_path(cache_key)
        
        if cache_file.exists() and not self.config.is_cache_expired(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass
        
        try:
            if version:
                url = f"{self.config.registry_url}/api/v1/packages/{name}/{version}"
            else:
                url = f"{self.config.registry_url}/api/v1/packages/{name}"
            
            response = requests.get(
                url,
                timeout=self.config.connection_timeout_seconds
            )
            
            if response.status_code == 200:
                info = response.json()
                
                # Cache result
                cache_file.parent.mkdir(parents=True, exist_ok=True)
                with open(cache_file, 'w') as f:
                    json.dump(info, f)
                
                return info
            
            return None
        
        except requests.RequestException:
            return None
    
    def _display_info(self, info: Dict[str, Any]) -> None:
        """Display package information.
        
        Args:
            info: Package info dictionary
        """
        name = info.get('name', 'Unknown')
        version = info.get('version', 'Unknown')
        description = info.get('description', 'No description')
        author = info.get('author', 'Unknown')
        license = info.get('license', 'Unlicensed')
        homepage = info.get('homepage', '')
        repository = info.get('repository', '')
        downloads = info.get('total_downloads', 0)
        created = info.get('created_at', 'Unknown')
        updated = info.get('updated_at', 'Unknown')
        
        print(f"\n{name}@{version}")
        print(f"{'=' * (len(name) + len(version) + 1)}\n")
        
        print(f"Description: {description}\n")
        
        print(f"Author:     {author}")
        print(f"License:    {license}")
        
        if homepage:
            print(f"Homepage:   {homepage}")
        
        if repository:
            print(f"Repository: {repository}")
        
        print(f"Downloads:  {downloads:,}")
        print(f"Created:    {created}")
        print(f"Updated:    {updated}")
        
        # Dependencies
        dependencies = info.get('dependencies', {})
        if dependencies:
            print(f"\nDependencies ({len(dependencies)}):")
            for dep_name, dep_version in dependencies.items():
                print(f"  - {dep_name}@{dep_version}")
        
        # Available versions
        versions = info.get('versions', [])
        if versions and len(versions) > 1:
            print(f"\nAvailable versions ({len(versions)}):")
            for v in versions[:10]:  # Show first 10
                print(f"  - {v}")
            if len(versions) > 10:
                print(f"  ... and {len(versions) - 10} more")
        
        print()
