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
