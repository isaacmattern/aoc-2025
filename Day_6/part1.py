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
  
  rows = []
  
  for line in input:
    row = []
    for token in line.split():
      row.append(token)
    rows.append(row)
    
  ans = 0
    
  for i in range(len(rows[0])):
    accumulator = 0
    multiplyFlag = False
    if rows[-1][i] == "*":
      accumulator = 1
      multiplyFlag = True
      
    for j in range(len(rows) - 1):
      if multiplyFlag:
        accumulator *= int(rows[j][i])
      else:
        accumulator += int(rows[j][i])
    
    ans += accumulator
        
  print(ans)      

solve()