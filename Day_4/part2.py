import sys

DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1],
              [0, -1 ],          [0, 1],
              [1, -1 ], [1, 0 ], [1, 1]]

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part2.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def removeRoll(r: int, c: int, grid: list[list]) -> None:
  numRows = len(grid)
  numCols = len(grid[0])
  
  for direction in DIRECTIONS:
    newR, newC = r + direction[0], c + direction[1]
    if ((newR >= 0 and newR < numRows) and
        (newC >= 0 and newC < numCols) and
        grid[newR][newC] != '.'):
      grid[newR][newC] -= 1
      
  grid[r][c] = '.'

def getNumAdjacent(r: int, c: int, grid: list[list]) -> int:
  numAdjacentRolls = 0
  numRows = len(grid)
  numCols = len(grid[0])
  
  for direction in DIRECTIONS:
    newR, newC = r + direction[0], c + direction[1]
    if ((newR >= 0 and newR < numRows) and
        (newC >= 0 and newC < numCols) and
        grid[newR][newC] == '@'):
      numAdjacentRolls += 1
  
  return numAdjacentRolls
        
def solve():
  
  input = getInput()
  
  inputGrid = []  
  for line in input:
    inputGrid.append(line.strip())
    
  numberGrid = []
  for r in range(len(inputGrid)):
    nextRow = []
    for c in range(len(inputGrid)):
      if inputGrid[r][c] == "@":
        numAdjacent = getNumAdjacent(r, c, inputGrid)
        nextRow.append(numAdjacent)
      else:
        nextRow.append('.')
    numberGrid.append(nextRow)
        
  ans = 0
  keepSearching = True
  while keepSearching:
    keepSearching = False
    for r in range(len(numberGrid)):
      for c in range(len(numberGrid)):
        if numberGrid[r][c] != '.' and numberGrid[r][c] < 4:
          removeRoll(r, c, numberGrid)
          keepSearching = True
          ans += 1
  
  print(ans)      

solve()