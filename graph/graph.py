class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = []

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v1 != v2:
                self.vertices[v1].append(v2)
                self.vertices[v2].append(v1)
            else:
                self.vertices[v1].append(v2)
        else:
            raise ValueError("Both vertices should already be in the graph.")


    def get_vertices(self):
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []

    def size(self):
        return len(self.vertices)
