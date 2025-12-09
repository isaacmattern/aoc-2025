import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part1.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def solve():
  
  input = getInput()
  
  redTiles = []  
  for line in input:
    x, y = line.strip().split(",")
    redTiles.append([x, y])
  
  largest = 0
  for i in range(len(redTiles)):
    for j in range(i + 1, len(redTiles)):
      width = abs(int(redTiles[i][0]) - int(redTiles[j][0])) + 1
      height = abs(int(redTiles[i][1]) - int(redTiles[j][1])) + 1
      rectangleArea = int(width * height)
      largest = max(largest, rectangleArea)
    
  print(largest)      

solve()