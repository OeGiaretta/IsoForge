from isoforge.core.mesh.mesh import Mesh
from isoforge.core.algorithms.lookup_tables import CASE_TRIANGLES
from isoforge.core.mesh.triangle import Triangle

from isoforge.core.algorithms.lookup_tables import EDGE_CONNECTIONS
from isoforge.core.algorithms.interpolate import Interpolate

class MarchingCubes:

    def generate(self, cube):

        mesh = Mesh()

        case = cube.case_index()

        if case not in CASE_TRIANGLES:
            raise NotImplementedError(
                f"Case {case} ainda não implementado"
            )

        triangle_edges = CASE_TRIANGLES[case]

        vertices = []

        for edge in triangle_edges:
            vertex = self._interpolate_edge(cube, edge)
            vertices.append(vertex)

        for vertex in vertices:
            print(vertex)
        
        triangle = Triangle(
            vertices[0],
            vertices[1],
            vertices[2]
        )

        mesh.add_triangle(triangle)

        print(f"Case index: {case}")
        print(f"Edges {triangle_edges}")

        return mesh


    def _interpolate_edge(self, cube, edge_index):

        a, b = EDGE_CONNECTIONS[edge_index]

        return Interpolate(
            cube.vertices[a],
            cube.vertices[b],
            cube.values[a],
            cube.values[b]
        )

