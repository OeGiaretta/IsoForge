from dataclasses import dataclass

from .vertex import Vertex

@dataclass
class Triangle:
    v1: Vertex
    v2: Vertex
    v3: Vertex