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
  
  # key = str, val = list[str]
  nodes = {}
  
  for line in input:
    trimmed = line.strip()
    input, outputs = trimmed.split(":")
    outputList = []
    for output in outputs.strip().split(" "):
      outputList.append(output)
    nodes[input] = outputList
    
  ans = 0
  def dfs(curr: str):
    if curr == "out":
      nonlocal ans
      ans += 1
    else:
      for nextNode in nodes[curr]:
        dfs(nextNode)
    
  dfs("you")  
  print(ans)      

solve()