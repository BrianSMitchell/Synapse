"""Dependency Resolution

Handles:
- Semantic version parsing and matching
- Dependency graph resolution
- Conflict detection
- Lock file generation
"""

import json
import requests
import re
from typing import Optional, Dict, List, Set, Tuple
from .config import CLIConfig


class SemanticVersion:
    """Represents a semantic version."""
    
    def __init__(self, version_str: str):
        """Initialize semantic version.
        
        Args:
            version_str: Version string (e.g., '1.2.3' or '1.2.3-beta.1')
        """
        self.original = version_str
        self.major = 0
        self.minor = 0
        self.patch = 0
        self.prerelease = None
        self.build = None
        
        self._parse(version_str)
    
    def _parse(self, version_str: str) -> None:
        """Parse version string.
        
        Args:
            version_str: Version string to parse
        """
        # Remove build metadata
        if '+' in version_str:
            version_str, self.build = version_str.split('+', 1)
        
        # Parse prerelease
        if '-' in version_str:
            version_part, self.prerelease = version_str.split('-', 1)
        else:
            version_part = version_str
        
        # Parse major.minor.patch
        try:
            parts = version_part.split('.')
            self.major = int(parts[0]) if len(parts) > 0 else 0
            self.minor = int(parts[1]) if len(parts) > 1 else 0
            self.patch = int(parts[2]) if len(parts) > 2 else 0
        except (ValueError, IndexError):
            pass
    
    def __str__(self) -> str:
        """Return version string."""
        return self.original
    
    def __eq__(self, other) -> bool:
        """Check version equality."""
        if isinstance(other, str):
            other = SemanticVersion(other)
        return (self.major == other.major and
                self.minor == other.minor and
                self.patch == other.patch and
                self.prerelease == other.prerelease)
    
    def __lt__(self, other) -> bool:
        """Check if version is less than."""
        if isinstance(other, str):
            other = SemanticVersion(other)
        
        if self.major != other.major:
            return self.major < other.major
        if self.minor != other.minor:
            return self.minor < other.minor
        if self.patch != other.patch:
            return self.patch < other.patch
        
        # Prerelease versions are less than release
        if self.prerelease and not other.prerelease:
            return True
        if not self.prerelease and other.prerelease:
            return False
        
        return self.prerelease < other.prerelease if self.prerelease else False
    
    def __le__(self, other) -> bool:
        """Check if version is less than or equal."""
        return self == other or self < other
    
    def __gt__(self, other) -> bool:
        """Check if version is greater than."""
        return not self <= other
    
    def __ge__(self, other) -> bool:
        """Check if version is greater than or equal."""
        return not self < other
    
    def matches_range(self, version_spec: str) -> bool:
        """Check if version matches specification.
        
        Args:
            version_spec: Version spec (e.g., '^1.2.3', '~1.2.3', '>=1.2.3')
            
        Returns:
            True if version matches spec
        """
        version_spec = version_spec.strip()
        
        # Exact version
        if not any(c in version_spec for c in ['^', '~', '>', '<', '=']):
            return self == version_spec
        
        # Caret: allows changes that do not modify left-most non-zero version
        if version_spec.startswith('^'):
            base = SemanticVersion(version_spec[1:])
            if base.major > 0:
                return (self >= base and 
                       self.major == base.major)
            elif base.minor > 0:
                return (self >= base and
                       self.major == base.major and
                       self.minor == base.minor)
            else:
                return self == base
        
        # Tilde: allows patch-level changes
        if version_spec.startswith('~'):
            base = SemanticVersion(version_spec[1:])
            return (self >= base and
                   self.major == base.major and
                   self.minor == base.minor)
        
        # Greater than or equal
        if version_spec.startswith('>='):
            return self >= SemanticVersion(version_spec[2:])
        
        # Greater than
        if version_spec.startswith('>'):
            return self > SemanticVersion(version_spec[1:])
        
        # Less than or equal
        if version_spec.startswith('<='):
            return self <= SemanticVersion(version_spec[2:])
        
        # Less than
        if version_spec.startswith('<'):
            return self < SemanticVersion(version_spec[1:])
        
        # Equals
        if version_spec.startswith('='):
            return self == SemanticVersion(version_spec[1:])
        
        return False


class DependencyResolver:
    """Resolves package dependencies."""
    
    def __init__(self, config: CLIConfig):
        """Initialize resolver.
        
        Args:
            config: CLI configuration
        """
        self.config = config
        self._version_cache: Dict[str, List[str]] = {}
    
    def resolve_version(self, name: str, version_spec: Optional[str] = None) -> Optional[str]:
        """Resolve package version.
        
        Args:
            name: Package name
            version_spec: Version specification (or None for latest)
            
        Returns:
            Resolved version or None if not found
        """
        # Get available versions
        versions = self._get_available_versions(name)
        if not versions:
            return None
        
        # If no spec, return latest
        if not version_spec:
            return versions[0]  # Assuming sorted descending
        
        # Find matching version
        for version in versions:
            if SemanticVersion(version).matches_range(version_spec):
                return version
        
        return None
    
    def _get_available_versions(self, name: str) -> List[str]:
        """Get available versions from registry.
        
        Args:
            name: Package name
            
        Returns:
            List of versions (sorted descending)
        """
        if name in self._version_cache:
            return self._version_cache[name]
        
        try:
            response = requests.get(
                f"{self.config.registry_url}/api/v1/packages/{name}/versions",
                timeout=self.config.connection_timeout_seconds
            )
            
            if response.status_code == 200:
                versions = response.json().get('versions', [])
                
                # Sort descending
                versions.sort(key=lambda v: SemanticVersion(v), reverse=True)
                
                self._version_cache[name] = versions
                return versions
        
        except requests.RequestException:
            pass
        
        return []
    
    def resolve_dependencies(self, name: str, version: str) -> Dict[str, str]:
        """Resolve all dependencies for a package.
        
        Args:
            name: Package name
            version: Package version
            
        Returns:
            Dictionary of dependencies
        """
        resolved = {}
        to_process = [(name, version)]
        processed = set()
        
        while to_process:
            current_name, current_version = to_process.pop(0)
            
            if (current_name, current_version) in processed:
                continue
            
            processed.add((current_name, current_version))
            
            # Get package metadata
            deps = self._get_package_dependencies(current_name, current_version)
            
            for dep_name, dep_spec in deps.items():
                resolved_version = self.resolve_version(dep_name, dep_spec)
                
                if resolved_version:
                    resolved[dep_name] = resolved_version
                    to_process.append((dep_name, resolved_version))
        
        return resolved
    
    def _get_package_dependencies(self, name: str, version: str) -> Dict[str, str]:
        """Get dependencies for a package version.
        
        Args:
            name: Package name
            version: Package version
            
        Returns:
            Dictionary of dependencies
        """
        try:
            response = requests.get(
                f"{self.config.registry_url}/api/v1/packages/{name}/{version}",
                timeout=self.config.connection_timeout_seconds
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('dependencies', {})
        
        except requests.RequestException:
            pass
        
        return {}
    
    def detect_conflicts(self, dependencies: Dict[str, Dict[str, str]]) -> List[Tuple[str, str, str]]:
        """Detect version conflicts in dependencies.
        
        Args:
            dependencies: Nested dictionary of dependencies
            
        Returns:
            List of (package, version1, version2) conflicts
        """
        conflicts = []
        
        # Flatten all versions for each package
        versions_by_package: Dict[str, Set[str]] = {}
        
        for package_deps in dependencies.values():
            for dep_name, dep_version in package_deps.items():
                if dep_name not in versions_by_package:
                    versions_by_package[dep_name] = set()
                versions_by_package[dep_name].add(dep_version)
        
        # Check for conflicts
        for package, versions in versions_by_package.items():
            if len(versions) > 1:
                versions_list = sorted(versions, key=lambda v: SemanticVersion(v))
                conflicts.append((package, versions_list[0], versions_list[-1]))
        
        return conflicts
