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
    digits = [0] * 12
    for i, digit in enumerate(bank):
      digitIndex = 0
      for j in range(12, 0, -1):
        if i <= bankLength - j and digit > digits[digitIndex]:
          digits[digitIndex] = digit
          for d in range(digitIndex + 1, 12):
            digits[d] = 0
          break
        digitIndex += 1
        
    bankJoltage = int("".join(str(digit) for digit in digits))
    ans += bankJoltage
      
  print(ans)      

solve()