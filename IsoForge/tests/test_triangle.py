from isoforge.core.mesh.vertex import Vertex
from isoforge.core.mesh.triangle import Triangle
from isoforge.core.mesh.mesh import Mesh


triangle = Triangle(
    Vertex(0, 0, 0),
    Vertex(1, 0, 0),
    Vertex(0, 1, 0),
)

mesh = Mesh()

mesh.add_triangle(triangle)

print(mesh.triangles[0])
print(mesh.triangle_count())