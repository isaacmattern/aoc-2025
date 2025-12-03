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
  
  print("Beginning of Input\n")
  
  for line in input:
    print(line)
    
  print("\nEnd of Input")
  
  ans = 0
  print(ans)      

solve()