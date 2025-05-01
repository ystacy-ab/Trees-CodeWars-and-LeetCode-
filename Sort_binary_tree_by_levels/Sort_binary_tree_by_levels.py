def tree_by_levels(node):
    if not node:
        return []
    result = []
    q = [node]
    i = 0
    while i < len(q):
        node = q[i]
        result.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        i += 1
    return result
