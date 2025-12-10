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
  
  redTiles = []  
  for line in input:
    x, y = line.strip().split(",")
    redTiles.append([int(x), int(y)])
    
  polygonEdgePoints = set()
  for i in range(len(redTiles)):
    first = i
    second = i-1 if i > 0 else len(redTiles) - 1
    
    x1, y1 = redTiles[first]
    x2, y2 = redTiles[second]
    if x1 == x2:
      if y2 > y1:
        for y in range(y1, y2 + 1):
          polygonEdgePoints.add((x1, y))
      else:
        for y in range(y2, y1 + 1):
          polygonEdgePoints.add((x1, y))
    else: # y1 == y2
      if x2 > x1:
        for x in range(x1, x2 + 1):
          polygonEdgePoints.add((x, y1))
      else:
        for x in range(x2, x1 + 1):
          polygonEdgePoints.add((x, y1))
          
  def validRectangle(corner1: list[int], corner2: list[int]) -> bool:
    # Determine if a rectangle is valid by drawing a rectangle directly "inside"
    # the rectangle we really want to check. If the "edges" intersect with the edges
    # of the polygon created by our input list of red tiles, the rectangle is not valid.
    lowX = min(corner1[0], corner2[0]) + 1
    highX = max(corner1[0], corner2[0]) - 1
    lowY = min(corner1[1], corner2[1]) + 1
    highY = max(corner1[1], corner2[1]) - 1
    
    for x in range(lowX, highX + 1):
      if (x, lowY) in polygonEdgePoints or (x, highY) in polygonEdgePoints:
        return False
          
    for y in range(lowY, highY + 1):
      if (lowX, y) in polygonEdgePoints or (highX, y) in polygonEdgePoints:
        return False
      
    return True
  
  # size, redTile1, redTile2
  rectanglesBySize = []
  for i in range(len(redTiles)):
    for j in range(i + 1, len(redTiles)):
        width = abs(int(redTiles[i][0]) - int(redTiles[j][0])) + 1
        height = abs(int(redTiles[i][1]) - int(redTiles[j][1])) + 1
        rectangleArea = int(width * height)
        rectanglesBySize.append((rectangleArea, redTiles[i], redTiles[j]))

  largest = 0
  count = 0
  rectanglesBySizeSorted = reversed(sorted(rectanglesBySize))
  for size, redTile1, redTile2 in rectanglesBySizeSorted:
    print(f"Rectangles checked: {count}")
    if validRectangle(redTile1, redTile2):
      largest = size
      break
    count += 1
    
  print(largest)      

solve()