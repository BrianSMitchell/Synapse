"""List Command - Show installed packages

Handles:
- Listing local packages
- Global package listing
- Dependency tree display
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
import argparse
from .config import CLIConfig


class ListCommand:
    """Handles package listing."""
    
    def __init__(self, config: CLIConfig):
        """Initialize list command.
        
        Args:
            config: CLI configuration
        """
        self.config = config
    
    def execute(self, args: argparse.Namespace) -> int:
        """Execute list command.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code
        """
        global_mode = getattr(args, 'global', False)
        depth = getattr(args, 'depth', 0)
        
        if global_mode:
            packages = self._list_global_packages()
        else:
            packages = self._list_local_packages()
        
        if not packages:
            print("No packages installed")
            return 0
        
        self._display_packages(packages, depth)
        return 0
    
    def _list_local_packages(self) -> Dict[str, str]:
        """List packages installed in current project.
        
        Returns:
            Dictionary of package names and versions
        """
        manifest_file = self.config.manifest_file
        
        if not manifest_file.exists():
            return {}
        
        try:
            with open(manifest_file, 'r') as f:
                manifest = json.load(f)
                return manifest.get('dependencies', {})
        except json.JSONDecodeError:
            return {}
    
    def _list_global_packages(self) -> Dict[str, str]:
        """List globally installed packages.
        
        Returns:
            Dictionary of package names and versions
        """
        packages = {}
        
        if not self.config.packages_dir.exists():
            return packages
        
        # Iterate through packages directory
        for pkg_dir in self.config.packages_dir.iterdir():
            if pkg_dir.is_dir():
                pkg_name = pkg_dir.name
                
                # Get latest version
                version_dirs = sorted(
                    [d.name for d in pkg_dir.iterdir() if d.is_dir()],
                    key=self._parse_version,
                    reverse=True
                )
                
                if version_dirs:
                    packages[pkg_name] = version_dirs[0]
        
        return packages
    
    def _display_packages(self, packages: Dict[str, str], depth: int = 0) -> None:
        """Display packages in a formatted list.
        
        Args:
            packages: Dictionary of packages
            depth: Dependency depth to display
        """
        if not packages:
            return
        
        print(f"\nInstalled packages ({len(packages)}):\n")
        
        for name, version in sorted(packages.items()):
            print(f"├─ {name}@{version}")
            
            # Show dependencies if requested
            if depth > 0:
                self._show_dependencies(name, version, depth - 1, indent="│  ")
        
        print()
    
    def _show_dependencies(self, name: str, version: str, depth: int, indent: str = "") -> None:
        """Recursively show package dependencies.
        
        Args:
            name: Package name
            version: Package version
            depth: Remaining depth to traverse
            indent: Indentation prefix
        """
        if depth < 0:
            return
        
        # Try to load package manifest
        pkg_path = self.config.packages_dir / name / version
        manifest_file = pkg_path / 'synapse.json'
        
        if not manifest_file.exists():
            return
        
        try:
            with open(manifest_file, 'r') as f:
                manifest = json.load(f)
                dependencies = manifest.get('dependencies', {})
        except (json.JSONDecodeError, IOError):
            return
        
        if not dependencies:
            return
        
        deps = list(dependencies.items())
        for i, (dep_name, dep_version) in enumerate(deps):
            is_last = i == len(deps) - 1
            prefix = "└─" if is_last else "├─"
            next_indent = indent + ("   " if is_last else "│  ")
            
            print(f"{indent}{prefix} {dep_name}@{dep_version}")
            
            if depth > 0:
                self._show_dependencies(dep_name, dep_version, depth - 1, next_indent)
    
    @staticmethod
    def _parse_version(version_str: str) -> tuple:
        """Parse version string for sorting.
        
        Args:
            version_str: Version string (e.g., '1.2.3')
            
        Returns:
            Tuple of version components for comparison
        """
        try:
            parts = version_str.split('.')
            return tuple(int(p) for p in parts[:3])
        except (ValueError, IndexError):
            return (0, 0, 0)
