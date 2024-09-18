import math

def calculator(expression):
  """
  This function runs a simple calculator that can handle basic arithmetic operations,
  as well as square root, sine, cosine, and tangent.
  """

  # Replace "sqrt" with "math.sqrt"
  expression = expression.replace("sqrt", "math.sqrt")

  # Replace "sin", "cos", "tan" with corresponding math functions
  expression = expression.replace("sin", "math.sin")
  expression = expression.replace("cos", "math.cos")
  expression = expression.replace("tan", "math.tan")
  expression = expression.replace("^", "**")
  expression = expression.replace("pi", "math.pi")
  expression = expression.replace("e", "math.e")

  result = eval(expression)
  return result


import numpy as np
import re

def parse_equation(equation):
    equation = equation.replace(" ", "")
    pattern = r'([-+]?\d*\.?\d*)(x|y)([-+]?\d*\.?\d*)([-=])([-+]?\d*\.?\d+)'
    
    match = re.match(pattern, equation)
    if match:
        a = float(match.group(1)) if match.group(1) not in ('', '+') else 1.0
        b = float(match.group(3)) if match.group(3) not in ('', '+') else 1.0
        c = float(match.group(5))
        
        if match.group(4) == '=':
            return a, b, c
        elif match.group(4) == '-':
            return a, -b, -c
    raise ValueError("Invalid equation format.")

def main(equations):

    # Parse equations
    A = []
    B = []
    
    for eq in equations:
        a, b, c = parse_equation(eq)
        A.append([a, b])
        B.append(c)

    # Convert to NumPy arrays
    A = np.array(A)
    B = np.array(B)

    # Solve the equations
    solution = np.linalg.solve(A, B)
    
    x, y = solution
    return (x,y)
