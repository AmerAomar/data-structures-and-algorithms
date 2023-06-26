import pytest
from hashtable import HashTable

@pytest.fixture
def hashtable():
    return HashTable()

def test_set_and_get(hashtable):
    hashtable.set('name', 'John')
    hashtable.set('age', 30)
    hashtable.set('city', 'New York')
    hashtable.set('country', 'USA')

    assert hashtable.get('name') == 'John'
    assert hashtable.get('age') == 30
    assert hashtable.get('city') == 'New York'
    assert hashtable.get('country') == 'USA'

def test_get_non_existing_key(hashtable):
    assert hashtable.get('occupation') is None

def test_has_key(hashtable):
    hashtable.set('name', 'John')
    hashtable.set('age', 30)

    assert hashtable.has('name') is True
    assert hashtable.has('age') is True
    assert hashtable.has('occupation') is False

def test_keys(hashtable):
    hashtable.set('name', 'John')
    hashtable.set('age', 30)
    hashtable.set('city', 'New York')
    hashtable.set('country', 'USA')

    keys = hashtable.keys()
    assert len(keys) == 4
    assert 'name' in keys
    assert 'age' in keys
    assert 'city' in keys
    assert 'country' in keys

