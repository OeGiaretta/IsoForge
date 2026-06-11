from isoforge.core.mesh.vertex import Vertex
from isoforge.core.algorithms.interpolation import Interpolation

p1 = Vertex(0, 0, 0)
p2 = Vertex(10, 0, 0)

result = Interpolation(
    p1,
    p2,
    -1,  # value1
    1    # value2
)

# Expected output: Vertex(x=5.0, y=0.0, z=0.0)
print(result)  
