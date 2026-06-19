from isoforge.core.algorithms.cube import Cube
from isoforge.core.algorithms.marching_cubes import MarchingCubes
from isoforge.core.mesh.vertex import Vertex

cube = Cube(
    vertices=[
        Vertex(0, 0, 0),
        Vertex(1, 0, 0),
        Vertex(1, 1, 0),
        Vertex(0, 1, 0),
        Vertex(0, 0, 1),
        Vertex(1, 0, 1),
        Vertex(1, 1, 1),
        Vertex(0, 1, 1),
    ],
    values=[
        -1,
         1,
         1,
         1,
         1,
         1,
         1,
         1,
    ]
)

mc = MarchingCubes()

mesh = mc.generate(cube)

print(f"Triângulos na malha: {mesh.triangle_count()}")