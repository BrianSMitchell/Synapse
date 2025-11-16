"""
Tests for lock file management functionality.
"""

import json
import tempfile
from pathlib import Path
import pytest
from datetime import datetime

from synapse.cli.lockfile import (
    DependencyLock,
    LockFileManager,
)


class TestDependencyLock:
    """Test DependencyLock data class."""
    
    def test_create_dependency_lock(self):
        """Test creating a DependencyLock."""
        dep = DependencyLock(
            name="numpy",
            version="1.21.0",
            checksum="abc123",
            resolved_from="^1.20.0",
        )
        
        assert dep.name == "numpy"
        assert dep.version == "1.21.0"
        assert dep.checksum == "abc123"
        assert dep.resolved_from == "^1.20.0"
        assert dep.dependencies == {}
    
    def test_dependency_lock_with_transitive(self):
        """Test DependencyLock with transitive dependencies."""
        dep = DependencyLock(
            name="flask",
            version="2.0.0",
            checksum="def456",
            resolved_from="^2.0.0",
            dependencies={"werkzeug": "2.0.0", "jinja2": "3.0.0"},
        )
        
        assert dep.dependencies == {
            "werkzeug": "2.0.0",
            "jinja2": "3.0.0",
        }
    
    def test_dependency_lock_to_dict(self):
        """Test converting DependencyLock to dict."""
        dep = DependencyLock(
            name="pytest",
            version="7.0.0",
            checksum="ghi789",
            resolved_from="^6.0.0",
            dependencies={"pluggy": "1.0.0"},
        )
        
        data = dep.to_dict()
        
        assert data["version"] == "7.0.0"
        assert data["checksum"] == "ghi789"
        assert data["resolved_from"] == "^6.0.0"
        assert data["dependencies"] == {"pluggy": "1.0.0"}
        assert "installed_at" in data
    
    def test_dependency_lock_from_dict(self):
        """Test creating DependencyLock from dict."""
        data = {
            "version": "1.0.0",
            "checksum": "xyz",
            "resolved_from": "^1.0.0",
            "dependencies": {"dep1": "1.0.0"},
            "installed_at": "2024-01-01T00:00:00",
        }
        
        dep = DependencyLock.from_dict("mylib", data)
        
        assert dep.name == "mylib"
        assert dep.version == "1.0.0"
        assert dep.checksum == "xyz"
        assert dep.dependencies == {"dep1": "1.0.0"}


class TestLockFileManager:
    """Test LockFileManager."""
    
    def test_lock_file_path(self):
        """Test lock file path computation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = LockFileManager(Path(tmpdir))
            expected_path = Path(tmpdir) / "synapse-lock.json"
            assert manager.lock_path == expected_path
    
    def test_exists_false_when_not_present(self):
        """Test exists() returns False when lock file doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = LockFileManager(Path(tmpdir))
            assert not manager.exists()
    
    def test_exists_true_when_present(self):
        """Test exists() returns True when lock file exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            lock_path = Path(tmpdir) / "synapse-lock.json"
            lock_path.write_text('{"lockfile_version": 1, "dependencies": {}}')
            
            manager = LockFileManager(Path(tmpdir))
            assert manager.exists()
    
    def test_load_empty_when_not_present(self):
        """Test load() returns empty dict when lock file doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = LockFileManager(Path(tmpdir))
            deps = manager.load()
            assert deps == {}
    
    def test_save_and_load(self):
        """Test save() and load() round-trip."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = LockFileManager(Path(tmpdir))
            
            # Create dependencies
            deps = {
                "numpy": DependencyLock(
                    name="numpy",
                    version="1.21.0",
                    checksum="abc123",
                    resolved_from="^1.20.0",
                    dependencies={"cython": "0.29.0"},
                )
            }
            
            # Save
            manager.save(deps)
            assert manager.exists()
            
            # Load
            loaded = manager.load()
            assert "numpy" in loaded
            assert loaded["numpy"].version == "1.21.0"
            assert loaded["numpy"].dependencies == {"cython": "0.29.0"}
    
    def test_load_malformed_file_raises_error(self):
        """Test load() raises ValueError for malformed JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            lock_path = Path(tmpdir) / "synapse-lock.json"
            lock_path.write_text("{ invalid json")
            
            manager = LockFileManager(Path(tmpdir))
            
            with pytest.raises(ValueError, match="malformed"):
                manager.load()
    
    def test_load_incompatible_version_raises_error(self):
        """Test load() raises ValueError for incompatible lock file version."""
        with tempfile.TemporaryDirectory() as tmpdir:
            lock_path = Path(tmpdir) / "synapse-lock.json"
            lock_path.write_text(json.dumps({
                "lockfile_version": 999,
                "dependencies": {}
            }))
            
            manager = LockFileManager(Path(tmpdir))
            
            with pytest.raises(ValueError, match="version"):
                manager.load()
    
    def test_add_dependency(self):
        """Test add_dependency()."""
        deps = {}
        manager = LockFileManager()
        
        result = manager.add_dependency(
            deps,
            name="requests",
            version="2.28.0",
            checksum="req123",
            resolved_from="^2.28.0",
            transitive_deps={"urllib3": "1.26.0"},
        )
        
        assert "requests" in result
        assert result["requests"].version == "2.28.0"
        assert result["requests"].dependencies == {"urllib3": "1.26.0"}
    
    def test_remove_dependency(self):
        """Test remove_dependency()."""
        deps = {
            "numpy": DependencyLock(
                name="numpy",
                version="1.21.0",
                checksum="abc",
                resolved_from="^1.21.0",
            )
        }
        manager = LockFileManager()
        
        result = manager.remove_dependency(deps, "numpy")
        
        assert "numpy" not in result
    
    def test_get_transitive_dependencies(self):
        """Test get_transitive_dependencies()."""
        manager = LockFileManager()
        
        deps = {
            "flask": DependencyLock(
                name="flask",
                version="2.0.0",
                checksum="flask123",
                resolved_from="^2.0.0",
                dependencies={"werkzeug": "2.0.0", "jinja2": "3.0.0"},
            ),
            "werkzeug": DependencyLock(
                name="werkzeug",
                version="2.0.0",
                checksum="wz123",
                resolved_from="^2.0.0",
                dependencies={"dataclasses": "0.6"},
            ),
            "jinja2": DependencyLock(
                name="jinja2",
                version="3.0.0",
                checksum="j2123",
                resolved_from="^3.0.0",
                dependencies={},
            ),
        }
        
        transitive = manager.get_transitive_dependencies(deps, "flask")
        
        assert "werkzeug" in transitive
        assert "jinja2" in transitive
        assert "dataclasses" in transitive
    
    def test_verify_integrity_success(self):
        """Test verify_integrity() with matching checksum."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a test file
            test_file = Path(tmpdir) / "test.tar.gz"
            test_file.write_bytes(b"test content")
            
            manager = LockFileManager()
            
            # Calculate actual checksum
            checksum = manager.calculate_checksum(test_file)
            
            # Create dependency with matching checksum
            deps = {
                "mylib": DependencyLock(
                    name="mylib",
                    version="1.0.0",
                    checksum=checksum,
                    resolved_from="^1.0.0",
                )
            }
            
            assert manager.verify_integrity(deps, test_file, "mylib")
    
    def test_verify_integrity_failure(self):
        """Test verify_integrity() with mismatched checksum."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.tar.gz"
            test_file.write_bytes(b"test content")
            
            manager = LockFileManager()
            
            deps = {
                "mylib": DependencyLock(
                    name="mylib",
                    version="1.0.0",
                    checksum="wrong_checksum",
                    resolved_from="^1.0.0",
                )
            }
            
            assert not manager.verify_integrity(deps, test_file, "mylib")
    
    def test_is_locked_returns_version(self):
        """Test is_locked() returns locked version."""
        manager = LockFileManager()
        
        deps = {
            "numpy": DependencyLock(
                name="numpy",
                version="1.21.0",
                checksum="abc",
                resolved_from="^1.20.0",
            )
        }
        
        is_locked, version = manager.is_locked(deps, "numpy", "^1.20.0")
        assert is_locked
        assert version == "1.21.0"
    
    def test_is_locked_false_for_missing(self):
        """Test is_locked() returns False for missing package."""
        manager = LockFileManager()
        
        is_locked, version = manager.is_locked({}, "numpy", "^1.20.0")
        assert not is_locked
        assert version is None
    
    def test_get_locked_version(self):
        """Test get_locked_version()."""
        manager = LockFileManager()
        
        deps = {
            "pytest": DependencyLock(
                name="pytest",
                version="7.0.0",
                checksum="pytest123",
                resolved_from="^6.0.0",
            )
        }
        
        version = manager.get_locked_version(deps, "pytest")
        assert version == "7.0.0"
    
    def test_get_locked_version_missing(self):
        """Test get_locked_version() for missing package."""
        manager = LockFileManager()
        
        version = manager.get_locked_version({}, "pytest")
        assert version is None
    
    def test_calculate_checksum(self):
        """Test calculate_checksum()."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.txt"
            test_file.write_bytes(b"hello world")
            
            manager = LockFileManager()
            checksum = manager.calculate_checksum(test_file)
            
            # Verify it's a valid hex string
            assert isinstance(checksum, str)
            assert len(checksum) == 64  # SHA256 produces 64 hex chars
            assert all(c in "0123456789abcdef" for c in checksum)
    
    def test_validate_lock_file_valid(self):
        """Test validate_lock_file() for valid lock file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = LockFileManager(Path(tmpdir))
            
            deps = {
                "numpy": DependencyLock(
                    name="numpy",
                    version="1.21.0",
                    checksum="abc",
                    resolved_from="^1.21.0",
                    dependencies={},
                )
            }
            
            manager.save(deps)
            
            is_valid, errors = manager.validate_lock_file()
            assert is_valid
            assert errors == []
    
    def test_validate_lock_file_missing_transitive(self):
        """Test validate_lock_file() detects missing transitive deps."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = LockFileManager(Path(tmpdir))
            
            deps = {
                "flask": DependencyLock(
                    name="flask",
                    version="2.0.0",
                    checksum="flask",
                    resolved_from="^2.0.0",
                    dependencies={"werkzeug": "2.0.0"},
                    # Note: werkzeug is not in deps dict
                )
            }
            
            manager.save(deps)
            
            is_valid, errors = manager.validate_lock_file()
            assert not is_valid
            assert any("werkzeug" in str(e) for e in errors)
    
    def test_export_to_manifest_direct_only(self):
        """Test export_to_manifest() with direct_only=True."""
        manager = LockFileManager()
        
        deps = {
            "numpy": DependencyLock(
                name="numpy",
                version="1.21.0",
                checksum="abc",
                resolved_from="^1.20.0",
            ),
            "pandas": DependencyLock(
                name="pandas",
                version="1.3.0",
                checksum="def",
                resolved_from="1.3.0",  # Exact version
            ),
        }
        
        manifest = manager.export_to_manifest(deps, direct_only=True)
        
        assert manifest["numpy"] == "^1.20.0"
        assert manifest["pandas"] == "1.3.0"
    
    def test_prune_unused(self):
        """Test prune_unused()."""
        manager = LockFileManager()
        
        deps = {
            "numpy": DependencyLock(
                name="numpy",
                version="1.21.0",
                checksum="abc",
                resolved_from="^1.21.0",
            ),
            "pandas": DependencyLock(
                name="pandas",
                version="1.3.0",
                checksum="def",
                resolved_from="^1.3.0",
            ),
            "scipy": DependencyLock(
                name="scipy",
                version="1.7.0",
                checksum="ghi",
                resolved_from="^1.7.0",
            ),
        }
        
        pruned = manager.prune_unused(deps, ["numpy", "pandas"])
        
        assert "numpy" in pruned
        assert "pandas" in pruned
        assert "scipy" not in pruned
    
    def test_update_timestamps(self):
        """Test update_timestamps()."""
        manager = LockFileManager()
        
        deps = {
            "numpy": DependencyLock(
                name="numpy",
                version="1.21.0",
                checksum="abc",
                resolved_from="^1.21.0",
                installed_at="2020-01-01T00:00:00",
            )
        }
        
        before = datetime.utcnow().isoformat()
        updated = manager.update_timestamps(deps)
        after = datetime.utcnow().isoformat()
        
        # Check timestamp is updated and reasonable
        new_ts = updated["numpy"].installed_at
        assert before <= new_ts <= after


class TestLockFileIntegration:
    """Integration tests for lock file management."""
    
    def test_full_workflow(self):
        """Test complete lock file workflow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = LockFileManager(Path(tmpdir))
            
            # Start with no lock file
            assert not manager.exists()
            
            # Create dependencies
            deps = {}
            deps = manager.add_dependency(
                deps,
                name="numpy",
                version="1.21.0",
                checksum="numpy123",
                resolved_from="^1.20.0",
                transitive_deps={"cython": "0.29.0"},
            )
            
            deps = manager.add_dependency(
                deps,
                name="cython",
                version="0.29.0",
                checksum="cython123",
                resolved_from="^0.29.0",
            )
            
            # Save
            manager.save(deps)
            assert manager.exists()
            
            # Load and verify
            loaded = manager.load()
            assert len(loaded) == 2
            assert loaded["numpy"].version == "1.21.0"
            assert loaded["cython"].version == "0.29.0"
            
            # Remove a dependency
            loaded = manager.remove_dependency(loaded, "cython")
            manager.save(loaded)
            
            # Reload and verify
            loaded = manager.load()
            assert "numpy" in loaded
            assert "cython" not in loaded
