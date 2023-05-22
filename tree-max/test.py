from node import Node
from treemax import BinaryTree

def test_find_maximum_value_empty_tree():
    tree = BinaryTree(None)
    assert tree.find_maximum_value() == None

def test_find_maximum_value_single_node():
    tree = BinaryTree(5)
    assert tree.find_maximum_value() == 5

def test_find_maximum_value():
    tree = BinaryTree(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)

    assert tree.find_maximum_value() == 11
