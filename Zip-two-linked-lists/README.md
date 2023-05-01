# Zip two linked list

Takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Whiteboard

![zip two linked list](/Zip-two-linked-lists/img.png)

## Approach & Efficiency

***Time -->***
O(n) because the function iterates through the longer list, and the number of iterations is proportional to the length of the longer list.

***Space -->***
 O(1) because the function modifies the input linked lists in-place, without creating any new data structures that depend on the input size.

### Solution

### Zip two linked list function

```python
class Node:
    '''
    Node class that has properties for the value stored in the Node, and a pointer to the next Node.

    '''
    def __init__(self, value, next=None):
        '''
        Constructor for Node class.
        '''
        self.value = value
        self.next = next

class LinkedList:
    '''
    Linked List class that has properties for the head of the list.
    '''
    def __init__(self):
        self.head = None

    def insert(self, value):
        '''
        Adds a new node with that value to the head of the list with an O(1) Time performance.
        '''
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

                

    def __str__(self):
        '''
        Returns: a string representing all the values in the Linked List, formatted as:
        '''
        if not self.head:
            return "null"
        current = self.head
        output = ""
        while current:
            output += "{" + str(current.value) + "} -> "
            current = current.next
        output += "null"
        return output

def zip_lists(list1, list2):
    '''
Takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    '''
    if not list1.head and not list2.head:
        return LinkedList()

    if not list1.head:
        return list2

    if not list2.head:
        return list1

    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next
        current1.next = current2
        if next1:
            current2.next = next1
        current1 = next1
        current2 = next2

    return list1


```

### Test file

```python
from zip_two_linked_list import zip_lists, LinkedList

import pytest

@pytest.mark.parametrize("list1_values, list2_values, expected_output", [
    ([1, 3, 2], [5, 9, 4], "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> null"),
    ([1, 3], [5, 9, 4], "{1} -> {5} -> {3} -> {9} -> {4} -> null"),
    ([1, 3, 2], [5, 9], "{1} -> {5} -> {3} -> {9} -> {2} -> null"),
    ([], [], "null"),
])
def test_zip_lists(list1_values, list2_values, expected_output):
    list1 = LinkedList()
    list2 = LinkedList()

    for value in list1_values:
        list1.insert(value)

    for value in list2_values:
        list2.insert(value)

    assert str(zip_lists(list1, list2)) == expected_output


```

### to install dependencies

```python
pip install -r requirements.txt
```
