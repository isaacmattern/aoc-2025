import sys

DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1],
              [0, -1 ],          [0, 1],
              [1, -1 ], [1, 0 ], [1, 1]]

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part1.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def canAccessRoll(r: int, c: int, grid: list[str]) -> bool:
  numAdjacentRolls = 0
  numRows = len(grid)
  numCols = len(grid[0])
  
  for direction in DIRECTIONS:
    newR, newC = r + direction[0], c + direction[1]
    if ((newR >= 0 and newR < numRows) and
        (newC >= 0 and newC < numCols) and
        grid[newR][newC] == '@'):
      numAdjacentRolls += 1
  
  return numAdjacentRolls < 4
        
def solve():
  
  input = getInput()
  
  grid = []  
  for line in input:
    grid.append(line.strip())
    
  ans = 0
  for r in range(len(grid)):
    for c in range(len(grid)):
      if grid[r][c] == "@" and canAccessRoll(r, c, grid):
        ans += 1
      
  print(ans)      

solve()