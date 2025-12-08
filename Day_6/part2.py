import sys

def getInput():
  
  if len(sys.argv) < 2:
    print("Usage: python3 part2.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def getTermsFromColumn(col: list[str]) -> list[int]:
  termLength = len(col[0])
  
  terms = [[] for _ in range(termLength)]
  for token in col:
    for i in range(termLength):
      if token[i]:
        terms[i].append(token[i])
  
  termStrings = ["".join(term) for term in terms]
  termNumbers = [int(term) for term in termStrings]
  return termNumbers

def solve():
  
  i = getInput()
  input = []
  for inputLine in i:
    input.append(inputLine)
  
  rows = []
  
  for line in input:
    row = []
    for token in line.split():
      row.append(token)
    rows.append(row)
    
  cols = []
  for i in range(len(rows[0])):
    col = []
      
    for j in range(len(rows) - 1):
      col.append(rows[j][i])
    
    cols.append(col)
    
  maxTokenLengthPerColumn = []
  for col in cols:
    maxTokenLengthPerColumn.append(max([len(token) for token in col]))
    
  rowsWithSpaces = []
  for i, row in enumerate(input):
    rowWithSpaces = []
    ptr = 0
    for tokenLength in maxTokenLengthPerColumn:
      rowWithSpaces.append(input[i][ptr:ptr+tokenLength])
      ptr += tokenLength + 1
    rowsWithSpaces.append(rowWithSpaces)
  
  rowsWithSpaces[-1] = [term.strip() for term in rowsWithSpaces[-1]]
  
  ans = 0
    
  for i in range(len(rowsWithSpaces[0])):
    accumulator = 0
    multiplyFlag = False
    if rowsWithSpaces[-1][i] == "*":
      accumulator = 1
      multiplyFlag = True
      
    colWithSpaces = []
      
    for j in range(len(rowsWithSpaces) - 1):
      colWithSpaces.append(rowsWithSpaces[j][i])
      
    terms = getTermsFromColumn(colWithSpaces)
    
    for term in terms:
      if multiplyFlag:
        accumulator *= term
      else:
        accumulator += term
    
    ans += accumulator
        
  print(ans)      

solve()