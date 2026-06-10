from isoforge.core.math.parser import EquationParser
from isoforge.core.fields.scalar_field import ScalarField

parser = EquationParser(
    "x**2 + y**2 + z**2 - 1"
)

field = ScalarField(
    parser.evaluate,
    bounds=(-2, 2),
    resolution=30
)

data = field.generate()
print(data.shape)
print(type(data))