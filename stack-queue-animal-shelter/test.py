import pytest
from Animal import Animal
from Animal_shelter import AnimalShelter

@pytest.fixture
def shelter():
    return AnimalShelter()

def test_enqueue_dog(shelter):
    dog = Animal("Max", "dog")
    shelter.enqueue(dog)
    assert shelter.dogs == [dog]

def test_enqueue_cat(shelter):
    cat = Animal("Fluffy", "cat")
    shelter.enqueue(cat)
    assert shelter.cats == [cat]

def test_dequeue_dog(shelter):
    dog1 = Animal("Max", "dog")
    dog2 = Animal("Buddy", "dog")
    cat = Animal("Fluffy", "cat")
    shelter.enqueue(dog1)
    shelter.enqueue(cat)
    shelter.enqueue(dog2)
    assert shelter.dequeue("dog") == dog1
    assert shelter.dogs == [dog2]

def test_dequeue_cat(shelter):
    dog = Animal("Max", "dog")
    cat1 = Animal("Fluffy", "cat")
    cat2 = Animal("Mittens", "cat")
    shelter.enqueue(dog)
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    assert shelter.dequeue("cat") == cat1
    assert shelter.cats == [cat2]

def test_dequeue_invalid_pref(shelter):
    dog = Animal("Max", "dog")
    cat = Animal("Fluffy", "cat")
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    assert shelter.dequeue("invalid") is None
