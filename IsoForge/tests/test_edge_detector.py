from isoforge.core.algorithms.edge_detector import active_edges

values = [
    -1,
     1,
     1,
    -1,

    -1,
     1,
     1,
    -1,
]

print(active_edges(values))