# Linked list

Linked List Implementation: Singly Linked Lists.

## Whiteboard

<!-- empty -->

## Approach & Efficiency

Time --> O(1) because there is no looping through the list.  
Space --> O(1) because there is no use of more space.

### Solution

### linked list file

```python
class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self,value):
           node1 = Node(value) 
           if self.head == None:
                self.head = node1
           else:
                node1.next = self.head
                self.head = node1

    def include(self,key):
         included = self.head
         if included is None:
              return False
         while included is not None:
              if included.value == key:
                   return True
              included = included.next
         if included is None:
              return False
         
    def __str__(self):
        output= ""
        if self.head is None:
            output = "the linked list is empty!"
        else:
            current = self.head
            while(current):
                output += f'{current.value}> '
                current = current.next
            
            output += "None"
        return output  
```

### Test file

```python
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
```

### to install dependencies

```python
pip install -r requirements.txt
```
