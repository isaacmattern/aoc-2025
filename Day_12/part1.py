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
  lines = []
  for line in input:
    lines.append(line.strip())   
    
  i = 0
  shapeSizes = []
  while "x" not in lines[i]:
    i += 1
    currShapeSize = 0
    while lines[i]:
      currShapeSize += lines[i].count("#")
      i += 1
    i += 1
    shapeSizes.append(currShapeSize)
    
  ans = 0
  while i < len(lines):
    line = lines[i]
    width = int(line[0:line.index("x")])
    height = int(line[line.index("x")+1:line.index(":")])
    areaAvailable = width * height
    
    numOfEachShape = [int(num) for num in line[line.index(' ')+ 1:].split(" ")]
    areaNeeded = 0
    for k, needed in enumerate(numOfEachShape):
      areaNeeded += needed * shapeSizes[k]
    
    if areaAvailable >= areaNeeded:
      ans += 1
    i += 1
    
  print(ans)

solve()