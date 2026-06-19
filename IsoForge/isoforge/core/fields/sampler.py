import numpy as np


class Sampler:

    def sample(self, scalar_field):

        min_bound, max_bound = scalar_field.bounds
        resolution = scalar_field.resolution

        xs = np.linspace(
            min_bound,
            max_bound,
            resolution
        )

        ys = np.linspace(
            min_bound,
            max_bound,
            resolution
        )

        zs = np.linspace(
            min_bound,
            max_bound,
            resolution
        )

        data = np.zeros(
            (resolution, resolution, resolution)
        )

        for i, x in enumerate(xs):
            for j, y in enumerate(ys):
                for k, z in enumerate(zs):

                    data[i, j, k] = scalar_field.function(
                        x,
                        y,
                        z
                    )

        return data