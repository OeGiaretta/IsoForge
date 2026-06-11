from .triangle import Triangle

class Mesh:
    def __init__(self):
        self.triangles = []
    
    def add_triangle(self, triangle: Triangle):
        self.triangles.append(triangle)
    
    def triangle_count(self):
        return len(self.triangles)
    