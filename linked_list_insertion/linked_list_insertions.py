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