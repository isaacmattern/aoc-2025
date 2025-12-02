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
  
  currentPosition = 50
  password = 0
  
  for line in input:
    direction, clicks = line[0], int(line[1:])
    
    if direction == "L":
      # Account for the case where the dial is already at zero, and we are turning the dial leftwards (the excursion into "negative territory" will cause a password increment, so we want to offset it)
      if currentPosition == 0:
        password -= 1
      
      currentPosition -= clicks
      while currentPosition < 0:
        currentPosition = 100 + currentPosition
        password += 1
        
      # Edge case for where dial gets rotated to, say, -200
      if currentPosition == 0:
        password += 1
    else:
      currentPosition += clicks
      
      while currentPosition > 99:
        currentPosition -= 100
        password += 1
        
  print(password)      

solve()