import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part2.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def canBeDivided(numberString: str, numSubdivisions: int) -> bool:
  substringLength = int(len(numberString) / numSubdivisions)
  firstSubstring = numberString[:substringLength]
  for i in range(1, numSubdivisions):
    start = i * substringLength
    end = (i+1) * substringLength
    nextSubstring = numberString[start:end]
    if firstSubstring != nextSubstring:
      return False
    
  return True

def valid(number: int) -> bool:
  numberString = str(number)
  if len(numberString) == 1:
    return True
  
  stringLength = len(numberString)
  for numSubdivisions in range(2, stringLength + 1):
    if stringLength % numSubdivisions == 0:
      if canBeDivided(numberString, numSubdivisions):
        return False
  
  return True

def solve():
  
  input = getInput()
  line = input.readline()
  rangeStrings = line.split(",")
  ranges = []
  for rangeString in rangeStrings:
    beginningString, endString = rangeString.split("-")
    ranges.append([int(beginningString), int(endString)])
  
  ans = 0
  
  for start, end in ranges:
    for number in range(start, end + 1):
      if not valid(number):
        ans += number
  
  print(ans)      

solve()