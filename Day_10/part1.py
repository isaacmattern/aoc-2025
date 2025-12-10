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
    
  machines = []
  for line in input:
    trimmedLine = line.strip()
    openParenIndex = trimmedLine.index("[")
    closeParenIndex = trimmedLine.index("]")
    openCurlyIndex = trimmedLine.index("{")
    closeCurlyIndex = trimmedLine.index("}")
    
    indicatorLightsTargetString = trimmedLine[openParenIndex+1:closeParenIndex]
    targetState = tuple([True if char == "#" else False for char in indicatorLightsTargetString])
    
    buttons = []
    buttonSchematicStrings = trimmedLine[closeParenIndex+2:openCurlyIndex-1]
    for buttonSchematic in buttonSchematicStrings.split(" "):
      numbersWithCommas = buttonSchematic[1:len(buttonSchematic)-1]
      button = tuple([int(num) for num in numbersWithCommas.split(",")])
      buttons.append(button)
    buttons = tuple(buttons)
      
    joltagesString = trimmedLine[openCurlyIndex+1:closeCurlyIndex]
    joltages = tuple([int(num) for num in joltagesString.split(",")])
    
    machines.append((targetState, buttons, joltages))
      
  ans = 0
  print(ans)      

solve()