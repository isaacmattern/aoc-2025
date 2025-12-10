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
    print("Usage: python3 part2.py <filename>")
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
    # Sort buttons by largest to smallest length (most "efficient" button presses)
    sortedButtons = reversed(sorted(buttons, key=len))
    buttons = tuple(sortedButtons)
      
    joltagesString = trimmedLine[openCurlyIndex+1:closeCurlyIndex]
    joltages = tuple([int(num) for num in joltagesString.split(",")])
    
    newMachine = Machine(targetState=targetState, buttons=buttons, joltages=joltages)
    machines.append(newMachine)
    
  return machines
  

def solve():
  input = getInput()
  machines = parseInput(input)
  
  def dfs(m: int, curr: list[int], i: int, buttonsPushed: int) -> int:
    if machines[m].joltages == tuple(curr):
      return buttonsPushed
    elif i == len(machines[m].buttons):
      return math.inf
    
    updatedButtons = curr.copy()
    recurse = True
    for buttonIndex in machines[m].buttons[i]:
      updatedButtons[buttonIndex] += 1
      if updatedButtons[buttonIndex] > machines[m].joltages[buttonIndex]:
        recurse = False
        break
    
    pushButton = math.inf
    if recurse:
      pushButton = dfs(m, updatedButtons, i, buttonsPushed + 1)
      
    doNotPushButton = dfs(m, curr, i + 1, buttonsPushed)
    return min(pushButton, doNotPushButton)
  
  minButtonPushesPerMachine = []
  for m in range(len(machines)):
    start = [0] * len(machines[m].targetState)
    minButtonPushesPerMachine.append(dfs(m, start, 0, 0))
    print(f"Completed {m+1} of {len(machines)} total machines.")
    
  print(sum(minButtonPushesPerMachine))      

solve()