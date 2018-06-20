class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value='default', **pos):
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
    self.vertexes = []

    def debug_create_test_data(self):
        debuf_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=60, y=140)

        debug_edge_1 = Edge(debug_vertex_2)  # 1 -> 2
        debug_vertex_1.edges.append(debug_edge_1)

        self.vertexes.extend([debug_vertex_1, debug_vertex_2])
