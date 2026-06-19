from isoforge.core.math.parser import EquationParser
from isoforge.core.fields.scalar_field import ScalarField
from isoforge.core.fields.sampler import Sampler
from isoforge.core.algorithms.mesh_builder import MeshBuilder


parser = EquationParser(
    "x**2 + y**2 + z**2 - 1"
)

field = ScalarField(
    parser.evaluate,
    bounds=(-2, 2),
    resolution=30
)

sampler = Sampler()

data = sampler.sample(field)

print(data.shape)
print(type(data))

builder = MeshBuilder()

mesh = builder.build(field)