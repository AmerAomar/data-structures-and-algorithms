from queue import Queue

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

    def breadth_first(self, starting_vertex):
        '''
        Return a list containing the vertices in a breadth-first order.
        '''
        q = Queue()
        visited = set()
        if starting_vertex not in self.vertices:
            raise ValueError("Vertex not in graph")
        q.put(starting_vertex)
        result = []

        while not q.empty():
            v = q.get()
            if v not in visited:
                visited.add(v)
                result.append(v)
                for neighbor in self.get_neighbors(v):
                    q.put(neighbor)

        return result


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_vertex("Metroville")
    graph.add_vertex("Monstropolis")
    graph.add_vertex("Narnia")
    graph.add_vertex("Naboo")
    graph.add_edge("Pandora", "Arendelle")
    graph.add_edge("Arendelle", "Metroville")
    graph.add_edge("Arendelle", "Monstropolis")
    graph.add_edge("Metroville", "Monstropolis")
    graph.add_edge("Metroville", "Narnia")
    graph.add_edge("Metroville", "Naboo")
    graph.add_edge("Monstropolis", "Naboo")
    graph.add_edge("Narnia", "Naboo")
    print(graph.breadth_first("Pandora"))
    print(graph.breadth_first("Arendelle"))