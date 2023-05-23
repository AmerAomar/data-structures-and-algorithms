# Linked list Insertions

Extend a Linked List to allow various insertion methods.

## Whiteboard

<!-- empty -->

## Approach & Efficiency

***Time -->***

**append O(n)** : because it may need to traverse the entire list to find the last node.

**insert_before O(n)**: because in the worst case they may need to traverse the entire list to find the node with the given value.

**insert_after  O(n)**:because in the worst case they may need to traverse the entire list to find the node with the given value.

***Space -->*** O(n) because the class stores a reference to the head node, and each node in the list stores a reference to the next node.

### Solution

### linked list insertion file

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class linked_list:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(value)

    def insert_before(self, value, new_value):
        if self.head is None:
            raise ValueError("List is empty")

        if self.head.value == value:
            self.head = Node(new_value, self.head)
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.value != value:
            current_node = current_node.next

        if current_node.next is None:
            raise ValueError("Value not found")

        current_node.next = Node(new_value, current_node.next)

    def insert_after(self, value, new_value):
        if self.head is None:
            raise ValueError("List is empty")

        current_node = self.head
        while current_node is not None and current_node.value != value:
            current_node = current_node.next

        if current_node is None:
            raise ValueError("Value not found")

        current_node.next = Node(new_value, current_node.next)
```

### Test file

```python
from linked_list_insertion.linked_list_insertions import linked_list

def test_append():
    lst = linked_list()
    lst.append(1)
    assert lst.head.value == 1
    lst.append(2)
    assert lst.head.next.value == 2
    lst.append(3)
    assert lst.head.next.next.value == 3


def test_insert_before():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.insert_before(2, 4)
    assert lst.head.value == 1
    assert lst.head.next.value == 4
    assert lst.head.next.next.value == 2
    assert lst.head.next.next.next.value == 3

def test_insert_before_first():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.insert_before(1, 3)
    assert lst.head.value == 3
    assert lst.head.next.value == 1
    assert lst.head.next.next.value == 2

def test_insert_after():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.insert_after(2, 4)
    assert lst.head.value == 1
    assert lst.head.next.value == 2
    assert lst.head.next.next.value == 4
    assert lst.head.next.next.next.value == 3

def test_insert_after_last():
    lst = linked_list()
    lst.append(1)
    lst.append(2)
    lst.insert_after(2, 3)
    assert lst.head.value == 1
    assert lst.head.next.value == 2
    assert lst.head.next.next.value == 3
    assert lst.head.next.next.next is None




```

### to install dependencies

```python
pip install -r requirements.txt
```
