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
    graph.add_edge("A", "B")
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
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
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
    graph.add_edge("A", "A")
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
    graph.add_edge("Pandora", "Arendelle")
    graph.add_edge("Arendelle", "Metroville")
    graph.add_edge("Arendelle", "Monstropolis")
    graph.add_edge("Metroville", "Monstropolis")
    graph.add_edge("Metroville", "Narnia")
    graph.add_edge("Metroville", "Naboo")
    graph.add_edge("Monstropolis", "Naboo")
    graph.add_edge("Narnia", "Naboo")
    assert graph.breadth_first("Pandora") == ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]

def test_breadth_first_disconnected_graph():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_edge("A", "B")
    graph.add_edge("C", "D")
    assert graph.breadth_first("A") == ["A", "B"]

def test_breadth_first_not_existent_vertex():
    graph = Graph()
    graph.add_vertex("A")
    with pytest.raises(ValueError):
        graph.breadth_first("B")


if __name__ == "__main__":
    pytest.main()