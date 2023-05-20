from binary_tree import BinaryTree
from node import Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(value, self.root)

    def _add_recursive(self, value, node):
        if value < node.value:
            if node.left:
                self._add_recursive(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add_recursive(value, node.right)
            else:
                node.right = Node(value)

    def contains(self, value):
        return self._contains_recursive(value, self.root)

    def _contains_recursive(self, value, node):
        if not node:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_recursive(value, node.left)
        else:
            return self._contains_recursive(value, node.right)
