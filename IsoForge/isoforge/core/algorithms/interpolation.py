from isoforge.core.mesh.vertex import Vertex

def Interpolation(
        p1: Vertex,
        p2: Vertex,
        value1: float,
        value2: float
):
    
    "Calculates the interpolation point between two vertices based on their values."

    if abs(value1 - value2) < 1e-6:
        return p1 
    
    t = (0 - value1) / (value2 - value1)

    x = p1.x + t * (p2.x - p1.x)
    y = p1.y + t * (p2.y - p1.y)
    z = p1.z + t * (p2.z - p1.z)
    return Vertex(x, y, z)

