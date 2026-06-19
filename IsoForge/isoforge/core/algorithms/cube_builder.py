from isoforge.core.algorithms.cube import Cube


class CubeBuilder:

    def create_cube(self, data, x, y, z):

        values = [
            data[x, y, z],
            data[x+1, y, z],
            data[x+1, y+1, z],
            data[x, y+1, z],

            data[x, y, z+1],
            data[x+1, y, z+1],
            data[x+1, y+1, z+1],
            data[x, y+1, z+1],
        ]

        return values