import sys
sys.path.insert(0, 'src')
from synapse.parser.parser import parse_and_execute

# Test simple 2D array
code = """
let grid = [[1,2],[3,4]]
let val = grid[0][1]
print(val)
"""

try:
    result = parse_and_execute(code)
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
