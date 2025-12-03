import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part2.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def solve():
  
  NUM_BATTERIES_TO_TURN_ON = 12
  input = getInput()
  
  banks = []
  for line in input:
    nextBank = []
    for char in line:
      if char != '\n':
        nextBank.append(int(char))
    banks.append(nextBank)
    
  bankLength = len(banks[0])
  
  ans = 0
  for bank in banks:
    digits = [0] * NUM_BATTERIES_TO_TURN_ON
    for i, digit in enumerate(bank):
      digitIndex = 0
      for j in range(NUM_BATTERIES_TO_TURN_ON, 0, -1):
        if i <= bankLength - j and digit > digits[digitIndex]:
          digits[digitIndex] = digit
          for d in range(digitIndex + 1, NUM_BATTERIES_TO_TURN_ON):
            digits[d] = 0
          break
        digitIndex += 1
        
    bankJoltage = int("".join(str(digit) for digit in digits))
    ans += bankJoltage
      
  print(ans)      

solve()