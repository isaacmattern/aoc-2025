import sys
import math

class Machine:
  def __init__(self, targetState: tuple[bool], buttons: tuple[tuple[int]], joltages: tuple[int]):
    if not isinstance(targetState, tuple) or not all(isinstance(x, bool) for x in targetState):
      raise ValueError("targetState must be a tuple of bools")

    if not isinstance(buttons, tuple) or not all(
        isinstance(b, tuple) and all(isinstance(x, int) for x in b)
        for b in buttons
    ):
      raise ValueError("buttons must be a tuple of tuples of ints")

    if not isinstance(joltages, tuple) or not all(isinstance(x, int) for x in joltages):
      raise ValueError("joltages must be a tuple of ints")

    self.targetState = targetState
    self.buttons = buttons
    self.joltages = joltages
    
def getInput():
  if len(sys.argv) < 2:
    print("Usage: python3 part1.py <filename>")
    quit()
    
  filename = sys.argv[1]
  input = open(filename, 'r')
  return input

def parseInput(input) -> list[Machine]:
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
    
    newMachine = Machine(targetState=targetState, buttons=buttons, joltages=joltages)
    machines.append(newMachine)
    
  return machines
  

def solve():
  input = getInput()
  machines = parseInput(input)
  
  def dfs(machine: Machine, curr: list[bool], i: int, buttonsPushed: int) -> int:
    if i == len(machine.buttons):
      if machine.targetState == tuple(curr):
        return buttonsPushed
      else:
        return math.inf
    
    updatedButtons = curr.copy()
    for buttonIndex in machine.buttons[i]:
      updatedButtons[buttonIndex] = not updatedButtons[buttonIndex]
    pushButton = dfs(machine, updatedButtons, i + 1, buttonsPushed + 1)
      
    doNotPushButton = dfs(machine, curr, i + 1, buttonsPushed)
    return min(pushButton, doNotPushButton)
  
  minButtonPushesPerMachine = []
  for machine in machines:
    start = [False] * len(machine.targetState)
    minButtonPushesPerMachine.append(dfs(machine, start, 0, 0))
    
  print(sum(minButtonPushesPerMachine))      

solve()