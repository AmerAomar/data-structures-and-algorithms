import pytest

from .linked_list import Linked_list

def test_zero():
    test = Linked_list()
    assert str(test) == "the linked list is empty!"

def test_first(data):
    assert str(data) == "C> B> A> None"

def test_second():
    test = Linked_list()
    test.insert("A")
    test.insert("B")
    assert str(test) == "B> A> None"

def test_third(data):
    assert data.include('A') == True

def test_fourth(data):
    assert data.include('test') == False

def test_fifth(data):
    assert data.head.value == "C"    

@pytest.fixture
def data():
    data = Linked_list()
    data.insert('A')
    data.insert('B')
    data.insert('C')
    return data