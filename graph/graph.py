from queue import Queue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = {}

    def add_edge(self, v1, v2, cost):
        if v1 in self.vertices and v2 in self.vertices:
            if v1 != v2:
                self.vertices[v1][v2] = cost
                self.vertices[v2][v1] = cost
            else:
                self.vertices[v1][v2] = cost
        else:
            raise ValueError("Both vertices should already be in the graph.")

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return list(self.vertices[vertex].keys())
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

    def business_trip(self, cities=[]):
        '''
        Determine whether the trip is possible with direct flights, and calculate the cost of the trip.
        '''
        cost = 0

        for i in range(len(cities) - 1):
            current_city = cities[i]
            next_city = cities[i + 1]

            if next_city in self.get_neighbors(current_city):
                if next_city in self.vertices[current_city]:
                    flight_cost = self.vertices[current_city][next_city]
                    cost += flight_cost
                else:
                    return None
            else:
                return None

        return f"${cost}"


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_vertex("Metroville")
    graph.add_vertex("Monstropolis")
    graph.add_vertex("Narnia")
    graph.add_vertex("Naboo")
    graph.add_edge("Pandora", "Arendelle", 50)
    graph.add_edge("Arendelle", "Metroville", 30)
    graph.add_edge("Arendelle", "Monstropolis", 20)
    graph.add_edge("Metroville", "Monstropolis", 10)
    graph.add_edge("Metroville", "Narnia", 40)
    graph.add_edge("Metroville", "Naboo", 60)
    graph.add_edge("Monstropolis", "Naboo", 25)
    graph.add_edge("Narnia", "Naboo", 35)
    print(graph.breadth_first("Pandora"))
    print(graph.breadth_first("Arendelle"))

    graph2 = Graph()
    graph2.add_vertex("Pandora")
    graph2.add_vertex("Arendelle")
    graph2.add_vertex("Metroville")
    graph2.add_vertex("Monstropolis")
    graph2.add_vertex("Narnia")
    graph2.add_vertex("Naboo")
    graph2.add_edge("Pandora", "Arendelle", 50)
    graph2.add_edge("Arendelle", "Metroville", 30)
    graph2.add_edge("Arendelle", "Monstropolis", 42)
    graph2.add_edge("Metroville", "Monstropolis", 10)
    graph2.add_edge("Metroville", "Narnia", 40)
    graph2.add_edge("Metroville", "Naboo", 60)
    graph2.add_edge("Monstropolis", "Naboo", 73)
    graph2.add_edge("Narnia", "Naboo", 35)
    print(graph2.business_trip(["Metroville", "Pandora"]))
    print(graph2.business_trip(["Arendelle", "Monstropolis", "Naboo"]))
    print(graph2.business_trip(["Naboo", "Pandora"]))
    print(graph2.business_trip(["Narnia", "Arendelle", "Naboo"]))
    print(graph2.business_trip(["Arendelle", "Metroville", "Monstropolis", "Naboo", "Narnia"]))
