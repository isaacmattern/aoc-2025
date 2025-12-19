import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

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
  
  # Note to self: Used Gemini LLM for this solution. Was unable to come up with a solution myself.
  # I knew it likely required a linear programming solution, but didn't know how to solve on my own. 
  def solveMachine(machine: Machine) -> int:
    num_buttons = len(machine.buttons)
    num_counters = len(machine.joltages)
    
    # 1. Objective function: Minimize sum(x_j), so coefficients are all 1
    c = np.ones(num_buttons)
    
    # 2. Build the Constraint Matrix A
    # A[i, j] = 1 if button j affects counter i, else 0
    A = np.zeros((num_counters, num_buttons))
    for j, button_indices in enumerate(machine.buttons):
      for i in button_indices:
        A[i, j] = 1
                
    # 3. Define the constraints: A @ x = target_joltages
    # SciPy MILP uses: lower_bound <= A @ x <= upper_bound
    # For equality, lower_bound == upper_bound
    targets = np.array(machine.joltages)
    constraints = LinearConstraint(A, targets, targets)
    
    # 4. Integrality constraints (1 means the variable must be an integer)
    integrality = np.ones(num_buttons)
    
    # 5. Bounds: x_j >= 0
    bounds = Bounds(0, np.inf)
    
    # Solve
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
    
    return int(round(res.fun))
  
  minButtonPushesPerMachine = []
  for m in range(len(machines)):
    buttonPresses = solveMachine(machines[m])
    minButtonPushesPerMachine.append(buttonPresses)
    
  print(sum(minButtonPushesPerMachine))      

solve()