import numpy as np

# This class represents a scalar field defined by a mathematical function. It generates a 3D grid of values based on the function and specified bounds and resolution.
class ScalarField:
    def __init__(
            self,
            function,
            bounds=(-2, 2),
            resolution=50
        ):

        self.function = function
        self.bounds = bounds
        self.resolution = resolution

    # This method generates a 3D grid of values by evaluating the function at each point in the grid defined by the bounds and resolution.
    def generate(self):
        xmin, xmax = self.bounds

        x = np.linspace(xmin, xmax, self.resolution)

        y = np.linspace(xmin, xmax, self.resolution)

        z = np.linspace(xmin, xmax, self.resolution)

        x, y, z = np.meshgrid(x, y, z, indexing="ij")

        values = self.function(x, y, z)

        return values