# First-in, First out Animal Shelter
<!-- Short summary or background information -->
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.

## Whiteboard Process
<!-- Embedded whiteboard image -->
on process

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time complexity:
***enqueue*** and ***dequeue*** operations in the AnimalShelter class is O(1), which means they take constant time to execute.

space complexity:

The space complexity of the enqueue operation is also O(1) because it adds a new animal to the end of the list without creating any additional data structures.

The space complexity of the dequeue operation is also O(1) because it removes the first animal from the list without creating any additional data structures.

## Solution

```python
from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal:Animal):
        if animal.species == "dog":
            self.dogs.append(animal)

        else:
            self.cats.append(animal)    


    def dequeue(self, pref):
        if pref == "dog" and self.dogs:
            return self.dogs.pop(0)
        
        elif pref == "cat" and self.cats:
            return self.cats.pop(0)
        
        else:
            return None
```

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
```
