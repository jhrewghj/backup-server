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
