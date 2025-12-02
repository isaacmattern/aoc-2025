import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part1.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def valid(number: int) -> bool:
  numberString = str(number)
  if len(numberString) % 2 == 1:
    return True
  
  halfwayPoint = int(len(numberString) / 2)
  firstHalf = numberString[:halfwayPoint]
  secondHalf = numberString[halfwayPoint:]
  
  return firstHalf != secondHalf

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