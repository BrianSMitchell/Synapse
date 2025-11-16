"""
Lock file management for Synapse package manager.

This module provides functionality for generating, reading, and managing
lock files that pin exact versions of dependencies for reproducible builds.

Lock files track:
- Exact versions of all dependencies
- Transitive dependencies (dependencies of dependencies)
- SHA256 checksums for integrity verification
- Timestamps for cache management
- Resolved version ranges that were used

A lock file ensures that `synapse pkg install` will always install
the exact same versions, enabling reproducible builds across environments.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from dataclasses import dataclass, asdict, field


@dataclass
class DependencyLock:
    """Represents a locked dependency in the lock file."""
    name: str
    version: str
    checksum: str
    resolved_from: str  # e.g., "^1.0.0" or "1.2.3"
    dependencies: Dict[str, str] = field(default_factory=dict)  # transitive deps
    installed_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "version": self.version,
            "checksum": self.checksum,
            "resolved_from": self.resolved_from,
            "dependencies": self.dependencies,
            "installed_at": self.installed_at,
        }
    
    @classmethod
    def from_dict(cls, name: str, data: Dict[str, Any]) -> "DependencyLock":
        """Create from dictionary data."""
        return cls(
            name=name,
            version=data["version"],
            checksum=data["checksum"],
            resolved_from=data.get("resolved_from", data["version"]),
            dependencies=data.get("dependencies", {}),
            installed_at=data.get("installed_at", datetime.utcnow().isoformat()),
        )


class LockFileManager:
    """
    Manages lock files for exact version pinning and reproducible builds.
    
    Lock files contain:
    - All dependencies (direct and transitive)
    - Exact pinned versions
    - SHA256 checksums for integrity
    - Original version ranges that were resolved
    - Installation timestamps
    
    Format: synapse-lock.json (JSON format for human readability)
    """
    
    LOCK_FILE_VERSION = 1
    LOCK_FILE_NAME = "synapse-lock.json"
    
    def __init__(self, project_root: Optional[Path] = None):
        """
        Initialize lock file manager.
        
        Args:
            project_root: Root directory of the project (default: current dir)
        """
        self.project_root = project_root or Path.cwd()
        self.lock_path = self.project_root / self.LOCK_FILE_NAME
    
    def exists(self) -> bool:
        """Check if a lock file exists."""
        return self.lock_path.exists()
    
    def load(self) -> Dict[str, DependencyLock]:
        """
        Load lock file from disk.
        
        Returns:
            Dictionary mapping package names to DependencyLock objects.
            Returns empty dict if lock file doesn't exist.
        
        Raises:
            ValueError: If lock file is malformed or incompatible version
        """
        if not self.exists():
            return {}
        
        try:
            with open(self.lock_path, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Lock file is malformed: {e}")
        
        # Validate version
        version = data.get("lockfile_version", 0)
        if version != self.LOCK_FILE_VERSION:
            raise ValueError(
                f"Lock file version {version} not supported. "
                f"Expected {self.LOCK_FILE_VERSION}"
            )
        
        # Load dependencies
        dependencies = {}
        for name, dep_data in data.get("dependencies", {}).items():
            dependencies[name] = DependencyLock.from_dict(name, dep_data)
        
        return dependencies
    
    def save(self, dependencies: Dict[str, DependencyLock]) -> None:
        """
        Save lock file to disk.
        
        Args:
            dependencies: Dictionary mapping package names to DependencyLock objects
        """
        lock_data = {
            "lockfile_version": self.LOCK_FILE_VERSION,
            "generated_at": datetime.utcnow().isoformat(),
            "dependencies": {
                name: dep.to_dict()
                for name, dep in dependencies.items()
            }
        }
        
        # Write with nice formatting
        with open(self.lock_path, 'w') as f:
            json.dump(lock_data, f, indent=2, sort_keys=True)
    
    def add_dependency(
        self,
        dependencies: Dict[str, DependencyLock],
        name: str,
        version: str,
        checksum: str,
        resolved_from: str = "",
        transitive_deps: Optional[Dict[str, str]] = None,
    ) -> Dict[str, DependencyLock]:
        """
        Add or update a dependency in the lock file.
        
        Args:
            dependencies: Current locked dependencies
            name: Package name
            version: Exact resolved version
            checksum: SHA256 checksum of the package
            resolved_from: Original version range (e.g., "^1.0.0")
            transitive_deps: Transitive dependencies as {name: version}
        
        Returns:
            Updated dependencies dictionary
        """
        dep = DependencyLock(
            name=name,
            version=version,
            checksum=checksum,
            resolved_from=resolved_from or version,
            dependencies=transitive_deps or {},
        )
        dependencies[name] = dep
        return dependencies
    
    def remove_dependency(
        self,
        dependencies: Dict[str, DependencyLock],
        name: str,
    ) -> Dict[str, DependencyLock]:
        """
        Remove a dependency from the lock file.
        
        Args:
            dependencies: Current locked dependencies
            name: Package name to remove
        
        Returns:
            Updated dependencies dictionary
        """
        dependencies.pop(name, None)
        return dependencies
    
    def get_transitive_dependencies(
        self,
        dependencies: Dict[str, DependencyLock],
        name: str,
    ) -> Dict[str, str]:
        """
        Get all transitive dependencies of a package.
        
        Args:
            dependencies: Locked dependencies
            name: Package name
        
        Returns:
            Dictionary of transitive dependencies {name: version}
        """
        if name not in dependencies:
            return {}
        
        result = {}
        to_process = [dependencies[name]]
        processed = set()
        
        while to_process:
            current = to_process.pop(0)
            if current.name in processed:
                continue
            processed.add(current.name)
            
            # Add transitive dependencies
            for dep_name, dep_version in current.dependencies.items():
                result[dep_name] = dep_version
                if dep_name in dependencies:
                    to_process.append(dependencies[dep_name])
        
        return result
    
    def verify_integrity(
        self,
        dependencies: Dict[str, DependencyLock],
        tarball_path: Path,
        package_name: str,
    ) -> bool:
        """
        Verify package integrity against lock file checksum.
        
        Args:
            dependencies: Locked dependencies
            tarball_path: Path to downloaded tarball
            package_name: Name of the package
        
        Returns:
            True if checksum matches, False otherwise
        """
        if package_name not in dependencies:
            return False
        
        expected_checksum = dependencies[package_name].checksum
        
        # Calculate SHA256 of tarball
        sha256_hash = hashlib.sha256()
        with open(tarball_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256_hash.update(chunk)
        
        calculated_checksum = sha256_hash.hexdigest()
        return calculated_checksum == expected_checksum
    
    def is_locked(
        self,
        dependencies: Dict[str, DependencyLock],
        name: str,
        version_spec: str,
    ) -> Tuple[bool, Optional[str]]:
        """
        Check if a dependency is locked to a specific version.
        
        Args:
            dependencies: Locked dependencies
            name: Package name
            version_spec: Version specification (e.g., "^1.0.0")
        
        Returns:
            Tuple of (is_locked, locked_version or None)
        """
        if name not in dependencies:
            return False, None
        
        locked = dependencies[name]
        
        # Check if the locked version matches the specification
        # This is a simple check - in practice would use version matching
        if version_spec == locked.resolved_from or version_spec == locked.version:
            return True, locked.version
        
        # Check if it's a range that includes the locked version
        # (simplified - real implementation would parse semver ranges)
        return True, locked.version
    
    def get_locked_version(
        self,
        dependencies: Dict[str, DependencyLock],
        name: str,
    ) -> Optional[str]:
        """
        Get the locked version of a package.
        
        Args:
            dependencies: Locked dependencies
            name: Package name
        
        Returns:
            Locked version or None if not found
        """
        dep = dependencies.get(name)
        return dep.version if dep else None
    
    def calculate_checksum(self, file_path: Path) -> str:
        """
        Calculate SHA256 checksum of a file.
        
        Args:
            file_path: Path to file
        
        Returns:
            Hex-encoded SHA256 checksum
        """
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    
    def validate_lock_file(self) -> Tuple[bool, List[str]]:
        """
        Validate the current lock file for consistency.
        
        Returns:
            Tuple of (is_valid, list of error messages)
        """
        if not self.exists():
            return True, []
        
        errors = []
        
        try:
            dependencies = self.load()
        except ValueError as e:
            return False, [str(e)]
        
        # Check for circular dependencies
        for name, dep in dependencies.items():
            visited = set()
            if self._has_circular_dependency(dependencies, name, visited):
                errors.append(f"Circular dependency detected for {name}")
        
        # Check that all transitive deps are in lock file
        for name, dep in dependencies.items():
            for trans_name in dep.dependencies:
                if trans_name not in dependencies:
                    errors.append(
                        f"Transitive dependency {trans_name} (from {name}) "
                        f"not found in lock file"
                    )
        
        return len(errors) == 0, errors
    
    def _has_circular_dependency(
        self,
        dependencies: Dict[str, DependencyLock],
        name: str,
        visited: set,
        rec_stack: Optional[set] = None,
    ) -> bool:
        """Check if there's a circular dependency."""
        rec_stack = rec_stack or set()
        
        visited.add(name)
        rec_stack.add(name)
        
        if name in dependencies:
            for dep_name in dependencies[name].dependencies:
                if dep_name not in visited:
                    if self._has_circular_dependency(
                        dependencies, dep_name, visited, rec_stack
                    ):
                        return True
                elif dep_name in rec_stack:
                    return True
        
        rec_stack.remove(name)
        return False
    
    def export_to_manifest(
        self,
        dependencies: Dict[str, DependencyLock],
        direct_only: bool = True,
    ) -> Dict[str, str]:
        """
        Export locked dependencies to manifest format.
        
        Args:
            dependencies: Locked dependencies
            direct_only: Only export direct dependencies if True
        
        Returns:
            Dictionary suitable for synapse.json dependencies field
        """
        result = {}
        
        for name, dep in dependencies.items():
            # If direct_only, use the resolved_from (original range)
            # Otherwise use exact version
            if direct_only and dep.resolved_from != dep.version:
                result[name] = dep.resolved_from
            else:
                result[name] = dep.version
        
        return result
    
    def prune_unused(
        self,
        dependencies: Dict[str, DependencyLock],
        keep_names: List[str],
    ) -> Dict[str, DependencyLock]:
        """
        Remove dependencies not in the keep list.
        
        Args:
            dependencies: Locked dependencies
            keep_names: List of package names to keep (including transitive)
        
        Returns:
            Pruned dependencies dictionary
        """
        keep_set = set(keep_names)
        return {
            name: dep
            for name, dep in dependencies.items()
            if name in keep_set
        }
    
    def update_timestamps(
        self,
        dependencies: Dict[str, DependencyLock],
    ) -> Dict[str, DependencyLock]:
        """
        Update installed_at timestamps for all dependencies.
        
        Args:
            dependencies: Locked dependencies
        
        Returns:
            Updated dependencies dictionary
        """
        now = datetime.utcnow().isoformat()
        for dep in dependencies.values():
            dep.installed_at = now
        return dependencies
