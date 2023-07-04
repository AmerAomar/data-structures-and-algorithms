import pytest
from tree_intersection import TreeNode, tree_intersection


def test_tree_intersection_empty_trees():
    tree1 = None
    tree2 = None
    result = tree_intersection(tree1, tree2)
    assert result == set()


def test_tree_intersection_one_empty_tree():
    # Create the binary tree: tree1
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    # Test with an empty tree (tree2)
    tree2 = None
    result = tree_intersection(tree1, tree2)
    assert result == set()


def test_tree_intersection_no_common_values():
 
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

  
    tree2 = TreeNode(4)
    tree2.left = TreeNode(5)
    tree2.right = TreeNode(6)

    result = tree_intersection(tree1, tree2)
    assert result == set()


def test_tree_intersection_with_common_values():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)
    tree1.right.right = TreeNode(6)

    
    tree2 = TreeNode(2)
    tree2.left = TreeNode(3)
    tree2.left.left = TreeNode(4)
    tree2.right = TreeNode(5)
    tree2.right.left = TreeNode(6)
    tree2.right.right = TreeNode(7)

    result = tree_intersection(tree1, tree2)
    assert result == {2, 3, 4, 5, 6}
