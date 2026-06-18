from isoforge.core.algorithms.cube import Cube
from isoforge.core.mesh.vertex import Vertex

cube = Cube(
    vertices=[
        Vertex(0, 0, 0)
        for _ in range(8)
    ],
    values=[
        -1,
        1,
        1,
        1,
        0,
        0,
        0,
        0
    ]
)
print(cube.case_index())  # Expected output: 1
