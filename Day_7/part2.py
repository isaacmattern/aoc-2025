import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part2.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def solve():
  
  input = getInput()
  
  grid = []
  for line in input:
    trimmedLine = line.strip().replace('S', '|')
    grid.append([char for char in trimmedLine])
      
  ans = 0
  
  for i in range(len(grid) - 1):
    for j in range(len(grid[0])):
      if grid[i][j] == "|":
        if grid[i+1][j] == "^":
          ans += 1
          if j-1 >= 0:
            grid[i+1][j-1] = "|"
          if j+1 < len(grid[0]):
            grid[i+1][j+1] = "|"
        else:
          grid[i+1][j] = "|"
      
  print(ans)      

solve()