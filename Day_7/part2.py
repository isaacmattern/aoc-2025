import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part2.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def visualizeGrid(grid: list[list]) -> None:
  for line in grid:
    charList = [str(char) if char != 0 else " " for char in line ]
    print("  ".join(charList))
  print()
  return

def solve():
  
  input = getInput()
  
  grid = []
  for line in input:
    lineList = []
    for char in line.strip():
      if char == 'S':
        lineList.append(1)
      elif char == '.':
        lineList.append(0)
      else:
        lineList.append(char)
    grid.append(lineList)
      
  ans = 0
  
  for i in range(len(grid) - 1):
    for j in range(len(grid[0])):
      if isinstance(grid[i][j], int) and grid[i][j] > 0:
        if grid[i+1][j] == "^":
          ans += 1
          if j-1 >= 0:
            grid[i+1][j-1] += grid[i][j]
          if j+1 < len(grid[0]):
            grid[i+1][j+1] += grid[i][j]
        else:
          grid[i+1][j] += grid[i][j]

  ans = 0
  for token in grid[-2]:
    if isinstance(token, int):
      ans += token
           
  print(ans)      

solve()