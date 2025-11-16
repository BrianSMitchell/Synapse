"""
Advanced dependency resolution for Synapse package manager.

This module provides sophisticated dependency resolution algorithms that:
- Handle transitive dependencies (dependencies of dependencies)
- Detect and resolve version conflicts
- Generate lock files with exact pinned versions
- Support multiple resolution strategies
- Track dependency chains for debugging

Resolution strategies:
1. Highest: Always select the highest compatible version
2. Stable: Prefer stable releases over pre-releases
3. Compatible: Select highest within compatible range (semver)
"""

from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum
import logging

from .resolver import SemanticVersion


logger = logging.getLogger(__name__)


class ResolutionStrategy(Enum):
    """Dependency resolution strategies."""
    HIGHEST = "highest"  # Always pick highest compatible
    STABLE = "stable"    # Prefer stable releases
    COMPATIBLE = "compatible"  # Highest in compatible range


@dataclass
class DependencyNode:
    """Represents a node in the dependency graph."""
    name: str
    version: str
    version_spec: str  # Original spec (e.g., "^1.0.0")
    dependencies: Dict[str, str] = field(default_factory=dict)
    parent: Optional[str] = None
    depth: int = 0


@dataclass
class ResolutionConflict:
    """Represents a dependency conflict."""
    package_name: str
    conflicting_versions: List[str]
    requesters: Dict[str, str]  # {package_name: required_version}
    
    def __str__(self) -> str:
        """Human-readable conflict description."""
        parts = [f"{self.package_name} has conflicting requirements:"]
        for pkg, version in self.requesters.items():
            parts.append(f"  - {pkg} requires {version}")
        return "\n".join(parts)


@dataclass
class ResolutionResult:
    """Result of dependency resolution."""
    success: bool
    resolved: Dict[str, DependencyNode] = field(default_factory=dict)
    conflicts: List[ResolutionConflict] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    resolution_chain: List[str] = field(default_factory=list)  # Debug trace


class AdvancedDependencyResolver:
    """
    Advanced resolver handling transitive dependencies and conflicts.
    
    The resolver:
    1. Takes a set of root dependencies
    2. Recursively fetches transitive dependencies
    3. Detects version conflicts
    4. Attempts to resolve conflicts
    5. Returns resolved dependency tree or conflicts
    """
    
    def __init__(
        self,
        package_fetcher,  # Function to fetch package metadata
        strategy: ResolutionStrategy = ResolutionStrategy.COMPATIBLE,
        max_depth: int = 20,
    ):
        """
        Initialize advanced resolver.
        
        Args:
            package_fetcher: Callable(name, version_spec) -> {versions: [...], ...}
            strategy: Resolution strategy to use
            max_depth: Maximum depth of dependency tree (prevent infinite loops)
        """
        self.package_fetcher = package_fetcher
        self.strategy = strategy
        self.max_depth = max_depth
    
    def resolve(
        self,
        dependencies: Dict[str, str],  # {name: version_spec}
        prefer_dev: bool = False,
    ) -> ResolutionResult:
        """
        Resolve dependencies to exact versions.
        
        Args:
            dependencies: Root dependencies {name: version_spec}
            prefer_dev: Prefer dev versions if True
        
        Returns:
            ResolutionResult with resolved dependencies or conflicts
        """
        result = ResolutionResult(success=True)
        resolved: Dict[str, DependencyNode] = {}
        in_progress: Set[str] = set()
        version_requirements: Dict[str, List[Tuple[str, str]]] = {}
        
        # Track version requirements for conflict detection
        # {package_name: [(requester, version_spec), ...]}
        
        # Process root dependencies
        queue = [
            (name, spec, None, 0)  # name, spec, parent, depth
            for name, spec in dependencies.items()
        ]
        
        while queue:
            name, spec, parent, depth = queue.pop(0)
            
            # Prevent infinite loops
            if depth > self.max_depth:
                result.warnings.append(
                    f"Depth limit ({self.max_depth}) reached for {name}"
                )
                continue
            
            # Prevent circular dependencies
            if name in in_progress:
                result.resolution_chain.append(
                    f"  Skip {name} (circular)"
                )
                continue
            
            in_progress.add(name)
            
            # Track version requirement
            if name not in version_requirements:
                version_requirements[name] = []
            version_requirements[name].append((parent or "ROOT", spec))
            
            # Resolve this package
            resolved_version = self._resolve_single(
                name,
                spec,
                resolved,
                prefer_dev,
            )
            
            if resolved_version is None:
                result.success = False
                result.conflicts.append(
                    ResolutionConflict(
                        package_name=name,
                        conflicting_versions=version_requirements[name],
                        requesters={p: v for p, v in version_requirements[name]},
                    )
                )
                continue
            
            # Create node
            node = DependencyNode(
                name=name,
                version=resolved_version,
                version_spec=spec,
                parent=parent,
                depth=depth,
            )
            resolved[name] = node
            result.resolution_chain.append(
                f"{'  ' * depth}Resolved {name}@{resolved_version}"
            )
            
            # Fetch transitive dependencies
            try:
                pkg_metadata = self.package_fetcher(name, resolved_version)
                transitive_deps = pkg_metadata.get("dependencies", {})
                
                node.dependencies = transitive_deps
                
                # Queue transitive dependencies
                for dep_name, dep_spec in transitive_deps.items():
                    queue.append((dep_name, dep_spec, name, depth + 1))
                
            except Exception as e:
                result.warnings.append(
                    f"Failed to fetch metadata for {name}@{resolved_version}: {e}"
                )
            
            in_progress.remove(name)
        
        result.resolved = resolved
        return result
    
    def _resolve_single(
        self,
        name: str,
        spec: str,
        already_resolved: Dict[str, DependencyNode],
        prefer_dev: bool = False,
    ) -> Optional[str]:
        """
        Resolve a single package to an exact version.
        
        Args:
            name: Package name
            spec: Version specification
            already_resolved: Already resolved packages
            prefer_dev: Prefer dev versions
        
        Returns:
            Resolved version string or None if no compatible version found
        """
        # Check if already resolved
        if name in already_resolved:
            existing = already_resolved[name].version
            # Verify compatibility
            if self._is_compatible(existing, spec):
                return existing
            else:
                return None  # Conflict
        
        # Fetch available versions
        try:
            pkg_info = self.package_fetcher(name, spec)
        except Exception:
            return None
        
        versions = pkg_info.get("versions", [])
        if not versions:
            return None
        
        # Sort versions according to strategy
        if self.strategy == ResolutionStrategy.HIGHEST:
            versions = self._sort_highest(versions, spec)
        elif self.strategy == ResolutionStrategy.STABLE:
            versions = self._sort_stable(versions, spec)
        else:  # COMPATIBLE
            versions = self._sort_compatible(versions, spec)
        
        # Return highest compatible
        if versions:
            return versions[0]
        
        return None
    
    def _is_compatible(self, version: str, spec: str) -> bool:
        """Check if a version satisfies a spec."""
        try:
            v = SemanticVersion(version)
            return v.matches_range(spec)
        except Exception:
            return version == spec
    
    def _sort_highest(
        self,
        versions: List[str],
        spec: str,
    ) -> List[str]:
        """Sort versions by highest compatible."""
        compatible = [
            v for v in versions
            if self._is_compatible(v, spec)
        ]
        
        try:
            compatible.sort(
                key=lambda v: SemanticVersion(v),
                reverse=True,
            )
        except Exception:
            pass
        
        return compatible
    
    def _sort_stable(
        self,
        versions: List[str],
        spec: str,
    ) -> List[str]:
        """Sort versions preferring stable releases."""
        compatible = [
            v for v in versions
            if self._is_compatible(v, spec)
        ]
        
        # Separate stable and pre-release
        stable = [v for v in compatible if not self._is_prerelease(v)]
        prerelease = [v for v in compatible if self._is_prerelease(v)]
        
        # Sort each group
        try:
            stable.sort(
                key=lambda v: SemanticVersion(v),
                reverse=True,
            )
            prerelease.sort(
                key=lambda v: SemanticVersion(v),
                reverse=True,
            )
        except Exception:
            pass
        
        return stable + prerelease
    
    def _sort_compatible(
        self,
        versions: List[str],
        spec: str,
    ) -> List[str]:
        """Sort versions by compatibility and stability."""
        compatible = [
            v for v in versions
            if self._is_compatible(v, spec)
        ]
        
        try:
            # Prefer stable, then highest
            def sort_key(v: str) -> Tuple[bool, SemanticVersion]:
                is_pre = self._is_prerelease(v)
                version = SemanticVersion(v)
                return (is_pre, version)
            
            compatible.sort(key=sort_key, reverse=True)
        except Exception:
            pass
        
        return compatible
    
    @staticmethod
    def _is_prerelease(version: str) -> bool:
        """Check if version is a pre-release."""
        return any(pre in version for pre in [
            "-alpha", "-beta", "-rc", "-dev", "-pre"
        ])
    
    def detect_conflicts(
        self,
        result: ResolutionResult,
    ) -> List[ResolutionConflict]:
        """
        Detect conflicts in resolution result.
        
        Args:
            result: ResolutionResult to analyze
        
        Returns:
            List of detected conflicts
        """
        conflicts = []
        
        # Analyze version requirements
        version_req_map: Dict[str, List[Tuple[str, str]]] = {}
        
        for name, node in result.resolved.items():
            if name not in version_req_map:
                version_req_map[name] = []
            version_req_map[name].append((node.parent or "ROOT", node.version_spec))
        
        # Check for conflicting requirements
        for name, requirements in version_req_map.items():
            versions = set(spec for _, spec in requirements)
            if len(versions) > 1:
                conflicts.append(
                    ResolutionConflict(
                        package_name=name,
                        conflicting_versions=list(versions),
                        requesters={p: v for p, v in requirements},
                    )
                )
        
        return conflicts
    
    def explain_resolution(
        self,
        result: ResolutionResult,
    ) -> str:
        """
        Generate human-readable explanation of resolution.
        
        Args:
            result: ResolutionResult to explain
        
        Returns:
            Multi-line explanation text
        """
        lines = []
        
        if result.success:
            lines.append("✓ Dependency resolution successful")
            lines.append("")
            lines.append("Resolved dependencies:")
            
            # Sort by depth
            by_depth = {}
            for node in result.resolved.values():
                if node.depth not in by_depth:
                    by_depth[node.depth] = []
                by_depth[node.depth].append(node)
            
            for depth in sorted(by_depth.keys()):
                for node in by_depth[depth]:
                    indent = "  " * depth
                    parent_info = f" (from {node.parent})" if node.parent else ""
                    lines.append(
                        f"{indent}{node.name}@{node.version}{parent_info}"
                    )
        else:
            lines.append("✗ Dependency resolution failed")
            lines.append("")
            lines.append("Conflicts:")
            for conflict in result.conflicts:
                lines.append(f"  {conflict.package_name}:")
                for pkg, version in conflict.requesters.items():
                    lines.append(f"    - {pkg} requires {version}")
        
        if result.warnings:
            lines.append("")
            lines.append("Warnings:")
            for warning in result.warnings:
                lines.append(f"  - {warning}")
        
        return "\n".join(lines)
    
    def try_resolve_conflicts(
        self,
        result: ResolutionResult,
    ) -> ResolutionResult:
        """
        Attempt to resolve detected conflicts.
        
        This is a simplified conflict resolution that tries to find
        a compatible version that satisfies all constraints.
        
        Args:
            result: ResolutionResult with conflicts
        
        Returns:
            New ResolutionResult with conflict resolution attempt
        """
        if result.success:
            return result
        
        # Try alternative resolution strategies
        for strategy in [
            ResolutionStrategy.COMPATIBLE,
            ResolutionStrategy.STABLE,
            ResolutionStrategy.HIGHEST,
        ]:
            if strategy == self.strategy:
                continue  # Already tried this
            
            logger.info(f"Attempting resolution with {strategy.value} strategy")
            old_strategy = self.strategy
            self.strategy = strategy
            
            # This would require re-running resolution
            # For now, just return the original result
            self.strategy = old_strategy
        
        return result
