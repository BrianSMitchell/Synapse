#!/usr/bin/env python
"""Verify Phase 16.3 implementation."""

import sys

def verify_imports():
    """Verify all classes can be imported."""
    try:
        from synapse.core.distributed_training import (
            AgentState,
            SyncMessage,
            LocalSyncCoordinator,
            DistributedAgent,
            DistributedTrainer,
            MPIDistributedTrainer,
            SparkDistributedTrainer,
            simple_loss_function,
            ackley_loss_function,
        )
        print("[OK] All imports successful")
        return True
    except ImportError as e:
        print(f"[FAIL] Import failed: {e}")
        return False


def verify_files():
    """Verify all files exist."""
    from pathlib import Path
    
    files = [
        "src/synapse/core/distributed_training.py",
        "tests/test_phase16_3_distributed_training.py",
        "src/synapse/cli/distributed_training_cmd.py",
        "docs/PHASE_16_3_DISTRIBUTED_TRAINING.md",
        "docs/PHASE_16_3_SUMMARY.md",
        "docs/DISTRIBUTED_TRAINING_QUICK_START.md",
    ]
    
    all_exist = True
    for filepath in files:
        path = Path(filepath)
        if path.exists():
            size = path.stat().st_size
            print(f"[OK] {filepath} ({size} bytes)")
        else:
            print(f"[FAIL] {filepath} NOT FOUND")
            all_exist = False
    
    return all_exist


def verify_core_classes():
    """Verify core class structure."""
    from synapse.core.distributed_training import (
        DistributedTrainer,
        DistributedAgent,
        LocalSyncCoordinator,
    )
    
    # Check DistributedTrainer
    trainer = DistributedTrainer(["agent1", "agent2"])
    assert len(trainer.agents) == 2
    print("[OK] DistributedTrainer instantiation works")
    
    # Check LocalSyncCoordinator
    coord = LocalSyncCoordinator()
    coord.register_agent("test")
    assert "test" in coord.message_queue
    print("[OK] LocalSyncCoordinator instantiation works")
    
    return True


def main():
    """Main verification."""
    print("=" * 70)
    print("PHASE 16.3 IMPLEMENTATION VERIFICATION")
    print("=" * 70)
    
    print("\n1. Verifying Files...")
    files_ok = verify_files()
    
    print("\n2. Verifying Imports...")
    imports_ok = verify_imports()
    
    print("\n3. Verifying Core Classes...")
    try:
        classes_ok = verify_core_classes()
    except Exception as e:
        print(f"✗ Class verification failed: {e}")
        classes_ok = False
    
    print("\n" + "=" * 70)
    if files_ok and imports_ok and classes_ok:
        print("PHASE 16.3 VERIFICATION: PASSED [SUCCESS]")
        print("=" * 70)
        return 0
    else:
        print("PHASE 16.3 VERIFICATION: FAILED [ERROR]")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
