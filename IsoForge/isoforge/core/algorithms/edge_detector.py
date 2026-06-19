from isoforge.core.algorithms.lookup_tables import EDGE_CONNECTIONS

def active_edges(values):
    edges = []

    for edge_index, (a, b) in enumerate(EDGE_CONNECTIONS):

        va = values[a]
        vb = values[b]
        if (va < 0 and vb > 0) or (va > 0 and vb < 0):
            edges.append(edge_index)
            
    return edges