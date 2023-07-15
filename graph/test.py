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

if __name__ == "__main__":
    pytest.main()