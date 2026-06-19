from isoforge.core.math.parser import EquationParser
from isoforge.core.fields.scalar_field import ScalarField
from isoforge.core.fields.sampler import Sampler
from isoforge.core.algorithms.cube_builder import CubeBuilder

parser = EquationParser(
    "x**2 + y**2 + z**2 - 1"
)

field = ScalarField(
    parser.evaluate,
    bounds=(-2, 2),
    resolution=5
)

data = Sampler().sample(field)

cube_values = CubeBuilder().create_cube(
    data,
    0,
    0,
    0
)

print(cube_values)
print(len(cube_values))