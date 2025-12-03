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
  
  ans = 0
  
  banks = []
  for line in input:
    nextBank = []
    for char in line:
      if char != '\n':
        nextBank.append(int(char))
    banks.append(nextBank)
    
  bankLength = len(banks[0])
  
  for bank in banks:
    digit1 = 0
    digit2 = 0
    for i, digit in enumerate(bank):
      if i < bankLength - 1 and digit > digit1:
        digit1 = digit
        digit2 = 0
      elif digit > digit2:
        digit2 = digit
      
    ans += (10 * digit1) + digit2
      
  print(ans)      

solve()