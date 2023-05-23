def breadth_first(tree): 
    result = [] 
    if tree is None:
        return result

    queue = []
    queue.append(tree) 

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result