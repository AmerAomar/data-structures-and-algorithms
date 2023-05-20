from binary_search_tree import BinarySearchTree

# Instantiate an empty tree
tree = BinarySearchTree()
print("Empty tree:")
print(tree.root)  # None

# Add nodes to the tree
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)
tree.add(8)

# Check if a value exists in the tree
print("Contains 5:", tree.contains(5))  # True
print("Contains 10:", tree.contains(10))  # False

# Perform depth-first traversals
print("Pre-order traversal:", tree.pre_order(tree.root, []))
# Output: [5, 3, 2, 4, 7, 6, 8]

print("In-order traversal:", tree.in_order(tree.root, []))
# Output: [2, 3, 4, 5, 6, 7, 8]

print("Post-order traversal:", tree.post_order(tree.root, []))
# Output: [2, 4, 3, 6, 8, 7, 5]
