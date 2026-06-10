from sympy import symbols
from sympy import sympify
from sympy import lambdify

# This class is responsible for parsing mathematical expressions and evaluating them.
class EquationParser:

    def __init__(self, expression: str):
        self.x, self.y, self.z = symbols("x y z")

        expr = sympify(expression)

        self.function = lambdify(
            (self.x, self.y, self.z), 
            expr, "numpy"
        )
    
    # This method evaluates the parsed function at given x, y, z coordinates.
    def evaluate(self, x, y, z):
        return self.function(x, y, z)