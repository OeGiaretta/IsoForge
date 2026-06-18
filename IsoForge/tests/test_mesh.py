from isoforge.core.mesh.vertex import Vertex
from isoforge.core.mesh.triangle import Triangle
from isoforge.core.mesh.mesh import Mesh

# Test the Mesh class
mesh = Mesh()

# Create a triangle and add it to the mesh
t = Triangle(
    Vertex(0, 0, 0),
    Vertex(1, 0, 0),
    Vertex(0, 1, 0)
)

mesh.add_triangle(t)

print(mesh.triangle_count())