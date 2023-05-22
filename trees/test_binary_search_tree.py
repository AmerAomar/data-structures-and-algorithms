import pytest
from binary_search_tree import BinarySearchTree


def test_instantiate_empty_tree():
    tree = BinarySearchTree()
    assert tree.root is None


def test_instantiate_tree_with_single_node():
    tree = BinarySearchTree()
    tree.add(5)
    assert tree.root.value == 5
    assert tree.root.left is None
    assert tree.root.right is None


def test_add_left_and_right_child_to_node():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.root.value == 5
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7


def test_pre_order_traversal():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    expected_result = [5, 3, 2, 4, 7, 6, 8]
    assert tree.pre_order(tree.root, []) == expected_result


def test_in_order_traversal():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    expected_result = [2, 3, 4, 5, 6, 7, 8]
    assert tree.in_order(tree.root, []) == expected_result


def test_post_order_traversal():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    expected_result = [2, 4, 3, 6, 8, 7, 5]
    assert tree.post_order(tree.root, []) == expected_result


def test_contains_existing_value():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.contains(5) is True
    assert tree.contains(3) is True
    assert tree.contains(7) is True


def test_contains_non_existing_value():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.contains(10) is False
    assert tree.contains(2) is False
    assert tree.contains(8) is False
