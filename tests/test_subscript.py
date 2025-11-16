#!/usr/bin/env python3
import sys
sys.path.insert(0, 'src')

code = '''
def test_sub(grid, i, j) {
    print("In test_sub: grid type =")
    print(grid)
    print("i =")
    print(i)
    print("j =")
    print(j)
    let val = grid[i][j]
    print("Got val =")
    print(val)
    val
}

let g = [[1, 2], [3, 4]]
let result = test_sub(g, 0, 1)
print("Result =")
print(result)
'''

from synapse.parser.parser import parse_and_execute
try:
    result = parse_and_execute(code)
except Exception as e:
    import traceback
    traceback.print_exc()
