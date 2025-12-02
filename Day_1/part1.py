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
  
  currentPosition = 50
  password = 0
  
  for line in input:
    direction, clicks = line[0], int(line[1:])
    
    if direction == "L":
      currentPosition -= clicks
      while currentPosition < 0:
        currentPosition = 100 + currentPosition
    else:
      currentPosition += clicks
      while currentPosition > 99:
        currentPosition -= 100
    
    if currentPosition == 0:
      password += 1
    
  print(password)      

solve()