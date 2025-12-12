import sys
from functools import cache

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part1.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def solve():
  
  input = getInput()
  
  # key = str, val = list[str]
  nodes = {}
  
  for line in input:
    trimmed = line.strip()
    input, outputs = trimmed.split(":")
    outputList = []
    for output in outputs.strip().split(" "):
      outputList.append(output)
    nodes[input] = outputList
    
  @cache
  def dfs(curr: str, fftFound: bool, dacFound: bool):
    if curr == "out":
      if fftFound and dacFound:
        return 1
      else:
        return 0
    else:
      total = 0
      for nextNode in nodes[curr]:
        total += dfs(nextNode, fftFound or nextNode == "fft", dacFound or nextNode == "dac")
      return total
      
  ans = dfs("svr", False, False)
  print(ans)      

solve()