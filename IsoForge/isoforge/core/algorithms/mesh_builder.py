from isoforge.core.fields.sampler import Sampler
from isoforge.core.mesh.mesh import Mesh

class MeshBuilder:

    def __init__(self):
        self.sampler = Sampler()

    def build(self, field):

        data = self.sampler.sample(field)

        nx, ny, nz = data.shape

        cube_count = 0

        for x in range(nx - 1):
            for y in range(ny - 1):
                for z in range(nz - 1):
                    cube_count += 1

        print(f"Grid: {nx}x{ny}x{nz}")
        print(f"Cubos encontrados: {cube_count}")

        return Mesh()