#!/usr/bin/env python
"""Simple test runner for Phase 16.3 distributed training tests."""

import sys
import subprocess

result = subprocess.run([
    sys.executable, "-m", "pytest", 
    "tests/test_phase16_3_distributed_training.py",
    "-v", "--tb=short", "-x"
], cwd=".")

sys.exit(result.returncode)
