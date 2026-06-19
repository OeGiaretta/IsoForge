EDGE_CONNECTIONS = [
    (0, 1),  # Edge 0
    (1, 2),  # Edge 1
    (2, 3),  # Edge 2
    (3, 0),  # Edge 3

    (4, 5),  # Edge 4
    (5, 6),  # Edge 5
    (6, 7),  # Edge 6
    (7, 4),  # Edge 7

    (0, 4),  # Edge 8
    (1, 5),  # Edge 9
    (2, 6),  # Edge 10
    (3, 7),  # Edge 11
]

CASE_TRIANGLES = {
    0: [],
    255: [],

    1: [0, 8, 3],
    254: [0, 3, 8],
}