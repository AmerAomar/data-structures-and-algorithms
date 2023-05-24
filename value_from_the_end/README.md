# k-th value from the end of a linked list

 linked list and a method kth_from_end(k) that returns the value of the node kth from the end of the list.

## Whiteboard

<!-- empty -->

## Approach & Efficiency

***Time -->***

**add() O(n)** : because the method must traverse the entire linked list to find the last node and add a new node after it.

**kth_from_end() O(n)**: because the method must first traverse the linked list to find the kth node from the beginning,Then, it must traverse the remaining nodes in the linked list to find the kth node from the end. Therefore, the total time complexity is O(n+n) = O(2n) = O(n).

***Space -->***
 O(n) because the class stores a reference to the head node, and each node in the linked list stores a reference to the next node.

### Solution

### value from the end file

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def kth_from_end(self, k):
        if k < 0:
            raise ValueError("k must be a non-negative integer")

        p1 = p2 = self.head
        for _ in range(k):
            if p2 is None:
                raise ValueError("k is greater than the length of the linked list")
            p2 = p2.next

        if p2 is None:
            raise ValueError("k is equal to the length of the linked list")

        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next

        return p1.value

```

### Test file

```python
import pytest
from .value_from_the_end import LinkedList

@pytest.mark.parametrize("lst, k, expected", [
    ([1, 3, 8, 2], 0, 2),
    ([1, 3, 8, 2], 1, 8),
    ([1, 3, 8, 2], 3, 1),
    ([1, 3, 8, 2], 4, ValueError),
    ([1, 3, 8, 2], 5, ValueError),
    ([1, 3, 8, 2], -1, ValueError),
    ([], 0, ValueError),
    ([1], 0, 1),
    ([1, 3, 8, 2, 5], 2, 8)
])
def test_kth_from_end(lst, k, expected):
    ll = LinkedList()
    for val in lst:
        ll.add(val)

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            ll.kth_from_end(k)
    else:
        assert ll.kth_from_end(k) == expected

```

### to install dependencies

```python
pip install -r requirements.txt
```
