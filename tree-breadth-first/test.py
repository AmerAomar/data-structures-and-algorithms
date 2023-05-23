from node import Node
from tree_breadth_first import breadth_first
def test_breadth_first():
    # Test case with a single node tree
    tree = Node(1)
    assert breadth_first(tree) == [1]

    # Test case with a complete binary tree
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    assert breadth_first(tree) == [1, 2, 3, 4, 5, 6, 7]

    # Test case with an empty tree
    tree = None
    assert breadth_first(tree) == []

    # Test case with a tree having only left children
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(3)
    tree.left.left.left = Node(4)
    assert breadth_first(tree) == [1, 2, 3, 4]

    # Test case with a tree having only right children
    tree = Node(1)
    tree.right = Node(2)
    tree.right.right = Node(3)
    tree.right.right.right = Node(4)
    assert breadth_first(tree) == [1, 2, 3, 4]

    # Test case with a tree having different levels
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.right.right = Node(5)
    tree.right.right.left = Node(6)
    assert breadth_first(tree) == [1, 2, 3, 4, 5, 6]

    # Test case for the example given in the challenge
    tree = Node(2)
    tree.left = Node(7)
    tree.right = Node(5)
    tree.left.left = Node(2)
    tree.left.right = Node(6)
    tree.right.right = Node(9)
    tree.left.right.left = Node(5)
    tree.left.right.right = Node(11)
    tree.right.right.left = Node(4)
    assert breadth_first(tree) == [2, 7, 5, 2, 6, 9, 5, 11, 4]
    