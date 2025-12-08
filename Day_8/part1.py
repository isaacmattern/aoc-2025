import sys
import heapq
import math

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part1.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def calculateDistance(node1: list[int], node2: list[int]) -> float:
  xDistanceSquared = (node1[0] - node2[0]) ** 2
  yDistanceSquared = (node1[1] - node2[1]) ** 2
  zDistanceSquared = (node1[2] - node2[2]) ** 2
  return math.sqrt(xDistanceSquared + yDistanceSquared + zDistanceSquared)

def solve():
  
  NUM_CONNECTIONS = 1000
  
  input = getInput()
  nodes = []
  for line in input:
    node = []
    for num in line.strip().split(","):
      node.append(int(num))
    nodes.append(node)
    
  connectionsHeap = []
  for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
      distance = calculateDistance(nodes[i], nodes[j])
      connectionsHeap.append([distance, i, j])
  heapq.heapify(connectionsHeap)
      
  nodes = [-1] * len(nodes)
  
  # Answers the question: "Who is the parent of this node"
  def find(node: int) -> int:
    if nodes[node] > 0:
      return find(nodes[node])
    else:
      return node
    
  # Makes both nodes have the same parent
  def union(node1: int, node2: int) -> int:
    node1Parent = find(node1)
    node2Parent = find(node2)
    if nodes[node1Parent] < nodes[node2Parent]:
      nodes[node1Parent] += nodes[node2Parent]
      
      nodes[node2Parent] = node1Parent
      # Path compression
      nodes[node2] = node1Parent
    else:
      nodes[node2Parent] += nodes[node1Parent]
      
      nodes[node1Parent] = node2Parent
      # Path compression
      nodes[node1] = node2Parent
      
  for _ in range(NUM_CONNECTIONS):
    _, node1, node2 = heapq.heappop(connectionsHeap)
    if find(node1) != find(node2):
      union(node1, node2)
      
  
  ans = 1
  # We want the "weight" of the three largest circuits which have been created
  sortedNodes = sorted(nodes)
  for i in range(3):
    ans *= sortedNodes[i]
  ans = abs(ans)
      
  print(ans)      

solve()