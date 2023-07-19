import pytest
from graph.graph import Graph

def test_add_vertex():
    graph = Graph()
    graph.add_vertex("A")
    assert graph.get_vertices() == ["A"]

def test_add_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", 10)
    assert graph.get_neighbors("A") == ["B"]
    assert graph.get_neighbors("B") == ["A"]

def test_get_vertices():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    assert graph.get_vertices() == ["A", "B", "C"]

def test_get_neighbors():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", 10)
    graph.add_edge("A", "C", 20)
    assert graph.get_neighbors("A") == ["B", "C"]
    assert graph.get_neighbors("B") == ["A"]
    assert graph.get_neighbors("C") == ["A"]

def test_size():
    graph = Graph()
    assert graph.size() == 0
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    assert graph.size() == 3

def test_single_vertex_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_edge("A", "A", 10)
    assert graph.get_neighbors("A") == ["A"]

def test_get_neighbors_nonexistent_vertex():
    graph = Graph()
    graph.add_vertex("A")
    assert graph.get_neighbors("B") == []

def test_breadth_first():
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
    assert graph.breadth_first("Pandora") == ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]

def test_breadth_first_disconnected_graph():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_edge("A", "B", 10)
    graph.add_edge("C", "D", 20)
    assert graph.breadth_first("A") == ["A", "B"]

def test_breadth_first_not_existent_vertex():
    graph = Graph()
    graph.add_vertex("A")
    with pytest.raises(ValueError):
        graph.breadth_first("B")

def test_business_trip():
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
    
 
    assert graph.business_trip(["Pandora", "Arendelle", "Metroville"]) == "$80"
    
    assert graph.business_trip(["Arendelle", "Monstropolis", "Naboo"]) == "$45"
  
    assert graph.business_trip(["Naboo", "Pandora"]) is None

    assert graph.business_trip(["Narnia", "Arendelle", "Naboo"]) is None

    assert graph.business_trip(["Arendelle", "Hogwarts", "Metroville"]) is None

    assert graph.business_trip([]) == "$0"




if __name__ == "__main__":
    pytest.main()
