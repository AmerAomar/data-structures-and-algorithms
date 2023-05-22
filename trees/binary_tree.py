class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, node, traversal):
        if node:
            traversal.append(node.value)
            self.pre_order(node.left, traversal)
            self.pre_order(node.right, traversal)
        return traversal

    def in_order(self, node, traversal):
        if node:
            self.in_order(node.left, traversal)
            traversal.append(node.value)
            self.in_order(node.right, traversal)
        return traversal

    def post_order(self, node, traversal):
        if node:
            self.post_order(node.left, traversal)
            self.post_order(node.right, traversal)
            traversal.append(node.value)
        return traversal
