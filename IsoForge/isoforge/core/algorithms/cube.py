from dataclasses import dataclass

from isoforge.core.mesh.vertex import Vertex

@dataclass
class Cube:
    vertices: list[Vertex]
    values: list[float]

    def case_index(self) -> int:

        "Calculates the case index for the cube based on the values at its vertices."
        
        index = 0
        
        for i, value in enumerate(self.values):
            
            if value > 0:
                index |= (1 << i)
            
        return index
