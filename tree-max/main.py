from node import Node
from treemax import BinaryTree


tree = BinaryTree(9)
tree.root.left = Node(1)
tree.root.right = Node(5)
tree.root.left.left = Node(100)
tree.root.left.right = Node(6)
tree.root.left.right.left = Node(45)
tree.root.left.right.right = Node(11)
tree.root.right.right = Node(49)
tree.root.right.right.left = Node(42)


maximum_value = tree.find_maximum_value()
print(maximum_value)  
