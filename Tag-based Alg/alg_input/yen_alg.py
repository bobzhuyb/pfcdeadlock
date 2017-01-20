"""
    Implementation of Dijkstra's and Yen's algorithm.
    Code taken from http://www.coolee.me/yen-k-shortest-path.html
"""

INFINITY = float('inf')


def __shortest_distance(G, D, U):
    """
        Get the shortest path from node in D to node in U

        @:param G   graph
        @:param D   mapping of nodes to their dist from start
        @:param U   unexplored nodes

        @:return source vertex in D, target vertex in U, distance from source to target
    """
    distance = INFINITY
    source_vertex, target_vertex = None, None
    for source, dist_start in D.items():
        for v, d in G[source].items():
            if v in U and dist_start + d < distance:
                source_vertex, target_vertex, distance = source, v, dist_start + d
    return source_vertex, target_vertex, distance


def predecessor_to_path(pred, source, target):
    """
        generate a path from source to target by pred
        @:param pred    a dict mapping each node to its predecessor node on the
        shortest path from the specified starting node:
        e.g. pred == {'b': 'a', 'c': 'b', 'd': 'c'}

        @:return    a list of the vertices in order along the shortest path.
        e.g. path = ['a', 'b', 'c', 'd']
    """
    v = target
    path = [v]
    while v != source:
        v = pred[v]
        path.append(v)
    path.reverse()
    return path


def dijkstra(G, source, target=None):
    """
        Find shortest paths from the start vertex to all vertices nearer than or
        equal to the end.

        The input graph G is assumed to have the following representation:
        A vertex can be any object that can be used as an index into a dictionary.
        G is a dictionary, indexed by vertices. For any vertex v, G[v] is itself
        a dictionary, indexed by the neighbors of v. For any edge v->w, G[v][w]
        is the length of the edge from v to w.

        The output is a pair (D,P) where D[v] is the distance from start to v and
        P[v] is the predecessor of v along the shortest path from s to v.

        e.g

        graph = {'a': {'b': 1},
        'b': {'c': 2, 'b': 5},
        'c': {'d': 1},
        'd': {}}
        Returns two dicts, `dist` and `pred`:

        dist, pred = dijkstra(graph, start='a')

        `dist` is a dict mapping each node to its shortest distance from the
        specified starting node:
        assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}

        `pred` is a dict mapping each node to its predecessor node on the
        shortest path from the specified starting node:
        assert pred == {'b': 'a', 'c': 'b', 'd': 'c'}

        Dijkstra's algorithm is only guaranteed to work correctly when all edge
        lengths are positive.
    """
    #print "call Dijkstra, src= , dst= ,", source, target
    # unexplored nodes
    U = set(G.keys())
    # mapping of nodes to their dist from start
    D = {source: 0}
    # mapping of nodes to their direct predecessors
    P = {}

    next_vertex = source
    U.remove(next_vertex)
    while U and not next_vertex == target:
        prev_vertex, next_vertex, distance = __shortest_distance(G, D, U)
        #print "prev_vertex, next_vertex, distance = ", prev_vertex, next_vertex, distance
        if next_vertex is None:
            break

        D[next_vertex] = distance
        P[next_vertex] = prev_vertex
        U.remove(next_vertex)
        #print "U = ", U
    return D, P


def dijkstra_shortest_path(G, source, target):
    """
    Find a single shortest path from the given start vertex to the given end vertex.

    The input has the same conventions as dijkstra().

    The output is a list of the vertices in order along the shortest path.
    e.g. path = ['a', 'b', 'c', 'd']
    """
    dist, pred = dijkstra(G, source, target)
    return (predecessor_to_path(pred, source, target),
            dist[target]) if target in pred else (None, INFINITY)


def yen_ksp(G, source, target, K=1):
    """
    Yen's algorithm computes single-source K-shortest loopless paths for a graph
    with non-negative edge cost.

    https://en.wikipedia.org/wiki/Yen's_algorithm

    @:param G   graph
    @:param source  source node
    @:param target  target node

    @:return a list of tuples that contains path and distance
    """

    # Determine the shortest path from the source to the target.
    # A = [(path[], dist[]), ...]
    A = []
    # Initialize the heap to store the potential kth shortest path.
    # B = [(path[], dist[]), ...]
    B = []

    dist, pred = dijkstra(G, source, target)
    if target in pred:
        A.append((predecessor_to_path(pred, source, target), dist))
    else:
        return None

    #print "K= ", K
    #print "A before ", A
    for k in range(1, K):
        # The previous k-shortest path
        last_path = A[-1][0]
        last_dist = A[-1][1]
        # The spur node ranges from the first node to the next to last node in
        # the previous k-shortest path.
        for i in range(0, len(last_path) - 1):
            spur_node = last_path[i]
            # The sequence of nodes from the source to the spur node of the
            # previous k-shortest path.
            root_path = last_path[:i + 1]
            root_distance = last_dist[spur_node]

            # Remove the links that are part of the previous shortest paths
            # which share the same root path.
            edges_removed = []
            for a in A:
                path = a[0]
                if (i + 1 < len(path) and path[:i + 1] == root_path and
                        path[i + 1] in G[spur_node]):
                    edges_removed.append(
                            (spur_node, path[i + 1], G[spur_node].pop(path[i + 1])))

                    # NOT removed each node in root_path from Graph;

            # Calculate the spur path from the spur node to the target
            dist, pred = dijkstra(G, spur_node, target)
            # Add the potential k-shortest path to the heap.
            if target in pred:
                # Entire path is made up of the root path and spur path.
                total_path = root_path[:-1] + predecessor_to_path(pred,
                        spur_node,
                        target)
                total_dist = {node: last_dist[node] for node in root_path}
                for node in dist.keys():
                    total_dist[node] = dist[node] + root_distance

                if (total_path, total_dist) not in B:
                    B.append((total_path, total_dist))

            # Add back the edges and nodes that were removed from the graph.
            for edge in edges_removed:
                G[edge[0]][edge[1]] = edge[2]

        # Add the lowest cost path becomes the k-shortest path.
        if B:
            B.sort(key=lambda p: p[1][target])
            A.append(B.pop(0))
        else:
            break

    #print "A after ", A
    return A
