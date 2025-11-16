#!/usr/bin/env python3
"""Run a Synapse file."""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from synapse.parser.parser import parse_and_execute

def run_file(filename):
    """Run a Synapse file."""
    try:
        with open(filename, 'r') as f:
            code = f.read()
        result = parse_and_execute(code)
        if result is not None and str(result) != 'None':
            print(result)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        import traceback
        print(f"Error: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python run_file.py <synapse_file>")
        sys.exit(1)
    run_file(sys.argv[1])
