class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    def build_tree_values(node, values):
        if node is None:
            return
        values.add(node.value)
        build_tree_values(node.left, values)
        build_tree_values(node.right, values)

    tree1_values = set()
    build_tree_values(tree1, tree1_values)

    common_values = set()

    def find_common_values(node):
        if node is None:
            return
        if node.value in tree1_values:
            common_values.add(node.value)
        find_common_values(node.left)
        find_common_values(node.right)

    find_common_values(tree2)

    return common_values
