from dataclasses import dataclass

# A vertex is a point in 3D space, defined by its x, y, and z coordinates.
@dataclass
class Vertex:
    x: float
    y: float
    z: float

    def as_tuplas(self):
        return(self.x, self.y, self.z)