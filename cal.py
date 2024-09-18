import math

def calculator(expression):
  """
  This function runs a simple calculator that can handle basic arithmetic operations,
  as well as square root, sine, cosine, and tangent.
  """

try:
  # Replace "sqrt" with "math.sqrt"
  expression = expression.replace("sqrt", "math.sqrt")

  # Replace "sin", "cos", "tan" with corresponding math functions
  expression = expression.replace("sin", "math.sin")
  expression = expression.replace("cos", "math.cos")
  expression = expression.replace("tan", "math.tan")

  result = eval(expression)
  print("Result:", result)

  except (SyntaxError, NameError, ZeroDivisionError) as e:
    print(f"Error: {e}")
    continue
