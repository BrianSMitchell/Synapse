#!/usr/bin/env python3
import sys
import traceback
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from synapse.parser.parser import parse_and_execute

code = '''
def count_neighbors(grid, x, y) {
    let count = 0
    let dxs = [-1, 0, 1]
    for dx in dxs {
        let dys = [-1, 0, 1]
        for dy in dys {
            if dx == 0 and dy == 0 {
            } else {
                let nx = x + dx
                let ny = y + dy
                if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 {
                    count = count + grid[nx][ny]
                }
            }
        }
    }
    count
}

let grid = [[0,0,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,1,1,1,0], [0,0,0,0,0]]
let neighbors = count_neighbors(grid, 2, 2)
print("Neighbors:")
print(neighbors)
'''

try:
    result = parse_and_execute(code)
    print(f"Final result: {result}")
except Exception as e:
    print(f"ERROR: {e}")
    traceback.print_exc()
