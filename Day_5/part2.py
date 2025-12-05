import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part2.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def combineRanges(ranges: list[list[int]]) -> list[list[int]]:
  sortedRanges = sorted(ranges)
  
  combinedRanges = [sortedRanges[0]]
  sortedRanges = sortedRanges[1:]
  
  for range in sortedRanges:
    if range[0] <= combinedRanges[-1][1]:
      combinedRanges[-1][1] = max(combinedRanges[-1][1], range[1])
    else:
      combinedRanges.append(range)
  
  return combinedRanges

def solve():
  
  input = getInput()
  
  ranges = []
  ids = []
  idsStarted = False
  for line in input:
    if not idsStarted:
      if line[0] == '\n':
        idsStarted = True
      else:
        trimmedRange = line.strip()
        beginningStr, endStr = trimmedRange.split('-')
        ranges.append([int(beginningStr), int(endStr)])
    else:
      ids.append(int(line.strip()))
      
  combinedRanges = combineRanges(ranges)
  ans = 0 
  
  for range in combinedRanges:
    ans += range[1] - range[0] + 1
    
  print(ans)      

solve()