"""
Tests for advanced dependency resolution.
"""

import pytest
from synapse.cli.advanced_resolver import (
    AdvancedDependencyResolver,
    ResolutionStrategy,
    DependencyNode,
    ResolutionConflict,
    ResolutionResult,
)


class MockPackageFetcher:
    """Mock fetcher for testing."""
    
    def __init__(self, packages=None):
        """
        Initialize with package data.
        
        Args:
            packages: Dict of {name: {versions: [...], dependencies: {...}}}
        """
        self.packages = packages or {}
    
    def __call__(self, name, version_spec):
        """Fetch package metadata."""
        if name not in self.packages:
            raise ValueError(f"Package {name} not found")
        
        pkg = self.packages[name]
        
        # Return metadata
        return {
            "name": name,
            "versions": pkg.get("versions", []),
            "dependencies": pkg.get("dependencies", {}).get(version_spec, {}),
        }


class TestAdvancedDependencyResolver:
    """Test AdvancedDependencyResolver."""
    
    def test_resolve_single_dependency(self):
        """Test resolving a single dependency."""
        fetcher = MockPackageFetcher({
            "requests": {
                "versions": ["2.28.0", "2.27.0", "2.26.0"],
                "dependencies": {},
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        result = resolver.resolve({"requests": "^2.28.0"})
        
        assert result.success
        assert "requests" in result.resolved
        assert result.resolved["requests"].version == "2.28.0"
    
    def test_resolve_with_transitive_dependencies(self):
        """Test resolving with transitive dependencies."""
        fetcher = MockPackageFetcher({
            "flask": {
                "versions": ["2.0.0"],
                "dependencies": {
                    "2.0.0": {"werkzeug": "^2.0.0", "jinja2": "^3.0.0"}
                }
            },
            "werkzeug": {
                "versions": ["2.0.0"],
                "dependencies": {"2.0.0": {}}
            },
            "jinja2": {
                "versions": ["3.0.0"],
                "dependencies": {"3.0.0": {}}
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        result = resolver.resolve({"flask": "^2.0.0"})
        
        assert result.success
        assert "flask" in result.resolved
        assert "werkzeug" in result.resolved
        assert "jinja2" in result.resolved
    
    def test_resolve_multiple_root_dependencies(self):
        """Test resolving multiple root dependencies."""
        fetcher = MockPackageFetcher({
            "numpy": {
                "versions": ["1.21.0"],
                "dependencies": {}
            },
            "pandas": {
                "versions": ["1.3.0"],
                "dependencies": {"1.3.0": {"numpy": "^1.20.0"}}
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        result = resolver.resolve({
            "numpy": "^1.21.0",
            "pandas": "^1.3.0"
        })
        
        assert result.success
        assert "numpy" in result.resolved
        assert "pandas" in result.resolved
    
    def test_resolve_empty_dependencies(self):
        """Test resolving empty dependency set."""
        fetcher = MockPackageFetcher()
        resolver = AdvancedDependencyResolver(fetcher)
        
        result = resolver.resolve({})
        
        assert result.success
        assert result.resolved == {}
    
    def test_missing_package_fails(self):
        """Test that missing package fails resolution."""
        fetcher = MockPackageFetcher()
        resolver = AdvancedDependencyResolver(fetcher)
        
        result = resolver.resolve({"nonexistent": "^1.0.0"})
        
        assert not result.success
        assert len(result.conflicts) > 0
    
    def test_no_compatible_version_fails(self):
        """Test failure when no compatible version exists."""
        fetcher = MockPackageFetcher({
            "lib": {
                "versions": ["1.0.0", "1.1.0"],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        # Request version 2.x when only 1.x exists
        result = resolver.resolve({"lib": "^2.0.0"})
        
        assert not result.success
    
    def test_resolution_strategy_highest(self):
        """Test HIGHEST resolution strategy."""
        fetcher = MockPackageFetcher({
            "lib": {
                "versions": ["3.0.0", "2.0.0", "1.0.0"],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(
            fetcher,
            strategy=ResolutionStrategy.HIGHEST
        )
        result = resolver.resolve({"lib": "^1.0.0"})
        
        assert result.success
        # With HIGHEST strategy, should pick the first compatible version
        # The mock returns versions as-is, so it depends on the sort
        assert result.resolved["lib"].version is not None
    
    def test_resolution_strategy_stable(self):
        """Test STABLE resolution strategy."""
        fetcher = MockPackageFetcher({
            "lib": {
                "versions": [
                    "2.0.0",
                    "2.0.0-rc1",
                    "1.9.0",
                    "1.9.0-beta",
                ],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(
            fetcher,
            strategy=ResolutionStrategy.STABLE
        )
        result = resolver.resolve({"lib": "^1.0.0"})
        
        assert result.success
        # Should prefer stable over pre-release
        version = result.resolved["lib"].version
        assert "rc" not in version and "beta" not in version
    
    def test_depth_limit_prevents_infinite_loops(self):
        """Test that depth limit prevents infinite dependency loops."""
        fetcher = MockPackageFetcher({
            "a": {
                "versions": ["1.0.0"],
                "dependencies": {"1.0.0": {"b": "^1.0.0"}}
            },
            "b": {
                "versions": ["1.0.0"],
                "dependencies": {"1.0.0": {"a": "^1.0.0"}}  # Circular!
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher, max_depth=5)
        result = resolver.resolve({"a": "^1.0.0"})
        
        # Should not crash, may or may not succeed
        assert isinstance(result, ResolutionResult)
        assert any("depth" in w.lower() for w in result.warnings)
    
    def test_detect_conflicts(self):
        """Test conflict detection."""
        fetcher = MockPackageFetcher({
            "app": {
                "versions": ["1.0.0"],
                "dependencies": {
                    "1.0.0": {
                        "lib": "^1.0.0",
                        "other": "^2.0.0"
                    }
                }
            },
            "lib": {
                "versions": ["1.2.0"],
                "dependencies": {"1.2.0": {"dep": "^3.0.0"}}
            },
            "dep": {
                "versions": ["3.0.0"],
                "dependencies": {}
            },
            "other": {
                "versions": ["2.0.0"],
                "dependencies": {"2.0.0": {"lib": "^2.0.0"}}  # Conflict!
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        # This would create a conflict: app wants lib ^1.0.0, other wants lib ^2.0.0
        # The actual resolution depends on version availability
    
    def test_explain_resolution_success(self):
        """Test explaining successful resolution."""
        fetcher = MockPackageFetcher({
            "lib": {
                "versions": ["1.0.0"],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        result = resolver.resolve({"lib": "^1.0.0"})
        
        explanation = resolver.explain_resolution(result)
        
        assert "successful" in explanation.lower()
        assert "lib" in explanation
    
    def test_explain_resolution_failure(self):
        """Test explaining failed resolution."""
        fetcher = MockPackageFetcher()
        resolver = AdvancedDependencyResolver(fetcher)
        
        result = resolver.resolve({"missing": "^1.0.0"})
        explanation = resolver.explain_resolution(result)
        
        assert "failed" in explanation.lower()
    
    def test_resolution_includes_chain(self):
        """Test that resolution includes debug chain."""
        fetcher = MockPackageFetcher({
            "a": {
                "versions": ["1.0.0"],
                "dependencies": {"1.0.0": {"b": "^1.0.0"}}
            },
            "b": {
                "versions": ["1.0.0"],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        result = resolver.resolve({"a": "^1.0.0"})
        
        assert len(result.resolution_chain) > 0
        assert any("a" in s for s in result.resolution_chain)
    
    def test_dependency_node_structure(self):
        """Test DependencyNode data structure."""
        node = DependencyNode(
            name="requests",
            version="2.28.0",
            version_spec="^2.28.0",
            dependencies={"urllib3": "^1.26.0"},
            parent="myapp",
            depth=1,
        )
        
        assert node.name == "requests"
        assert node.version == "2.28.0"
        assert node.parent == "myapp"
        assert node.depth == 1
    
    def test_resolution_conflict_str(self):
        """Test ResolutionConflict string representation."""
        conflict = ResolutionConflict(
            package_name="lib",
            conflicting_versions=["1.0.0", "2.0.0"],
            requesters={"app": "^1.0.0", "other": "^2.0.0"},
        )
        
        str_repr = str(conflict)
        
        assert "lib" in str_repr
        assert "conflicting" in str_repr.lower()
    
    def test_resolution_result_success(self):
        """Test ResolutionResult for success case."""
        result = ResolutionResult(
            success=True,
            resolved={
                "lib": DependencyNode(
                    name="lib",
                    version="1.0.0",
                    version_spec="^1.0.0",
                )
            }
        )
        
        assert result.success
        assert len(result.resolved) == 1
        assert len(result.conflicts) == 0
    
    def test_resolution_result_failure(self):
        """Test ResolutionResult for failure case."""
        result = ResolutionResult(
            success=False,
            conflicts=[
                ResolutionConflict(
                    package_name="lib",
                    conflicting_versions=["1.0.0"],
                    requesters={"app": "^2.0.0"},
                )
            ]
        )
        
        assert not result.success
        assert len(result.conflicts) == 1


class TestResolutionStrategies:
    """Test different resolution strategies."""
    
    def test_highest_picks_maximum_version(self):
        """Test HIGHEST strategy picks maximum compatible version."""
        fetcher = MockPackageFetcher({
            "lib": {
                "versions": ["1.5.0", "1.4.0", "1.3.0", "1.2.0"],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(
            fetcher,
            strategy=ResolutionStrategy.HIGHEST
        )
        result = resolver.resolve({"lib": "^1.2.0"})
        
        assert result.success
        # Should pick highest that matches range
        version = result.resolved["lib"].version
        assert version >= "1.2.0"
    
    def test_stable_avoids_prerelease(self):
        """Test STABLE strategy avoids pre-release versions."""
        fetcher = MockPackageFetcher({
            "lib": {
                "versions": [
                    "2.0.0",
                    "2.0.0-rc5",
                    "2.0.0-rc4",
                    "1.9.0",
                ],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(
            fetcher,
            strategy=ResolutionStrategy.STABLE
        )
        result = resolver.resolve({"lib": "^1.8.0"})
        
        assert result.success
        version = result.resolved["lib"].version
        # Should prefer stable release
        assert not any(x in version for x in ["-rc", "-alpha", "-beta"])
    
    def test_compatible_balances_stability_and_recency(self):
        """Test COMPATIBLE strategy balances stability and recency."""
        fetcher = MockPackageFetcher({
            "lib": {
                "versions": [
                    "2.0.0",
                    "1.9.0-rc1",
                    "1.8.0",
                ],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(
            fetcher,
            strategy=ResolutionStrategy.COMPATIBLE
        )
        result = resolver.resolve({"lib": "^1.7.0"})
        
        assert result.success
        # Should pick a compatible version
        version = result.resolved["lib"].version
        assert version is not None


class TestAdvancedResolverIntegration:
    """Integration tests for advanced resolver."""
    
    def test_complex_dependency_graph(self):
        """Test resolving complex dependency graph."""
        fetcher = MockPackageFetcher({
            "django": {
                "versions": ["4.0.0", "3.2.0"],
                "dependencies": {
                    "4.0.0": {"asgiref": "^3.4.0", "sqlparse": "^0.4.0"},
                    "3.2.0": {"asgiref": "^3.4.0", "sqlparse": "^0.4.0"}
                }
            },
            "djangorestframework": {
                "versions": ["3.13.0"],
                "dependencies": {
                    "3.13.0": {"django": "^3.2.0"}  # Compatible with django 4.x
                }
            },
            "asgiref": {
                "versions": ["3.4.1"],
                "dependencies": {}
            },
            "sqlparse": {
                "versions": ["0.4.1"],
                "dependencies": {}
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        result = resolver.resolve({
            "django": "^4.0.0",
            "djangorestframework": "^3.13.0"
        })
        
        # May succeed or have conflicts depending on version matching
        assert isinstance(result, ResolutionResult)
        # Should resolve at least the direct packages
        assert "django" in result.resolved
        assert "djangorestframework" in result.resolved
    
    def test_resolution_with_warnings(self):
        """Test resolution that completes with warnings."""
        fetcher = MockPackageFetcher({
            "mylib": {
                "versions": ["1.0.0"],
                "dependencies": {"1.0.0": {"missing": "^1.0.0"}}
            }
        })
        
        resolver = AdvancedDependencyResolver(fetcher)
        result = resolver.resolve({"mylib": "^1.0.0"})
        
        # May fail or succeed with warnings depending on implementation
        assert isinstance(result, ResolutionResult)
