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
  line = input.readline()
  rangeStrings = line.split(",")
  ranges = []
  for rangeString in rangeStrings:
    beginningString, endString = rangeString.split("-")
    ranges.append([int(beginningString), int(endString)])
  
  ans = 0

  print(ans)      

solve()