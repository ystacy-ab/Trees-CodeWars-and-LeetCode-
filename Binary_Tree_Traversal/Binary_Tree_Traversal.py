# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    lst, result = [node], []
    while lst:
        node = lst.pop()
        result.append(node.data)
        if node.right:
            lst.append(node.right)
        if node.left:
            lst.append(node.left)
    return result

# In-order traversal
def in_order(node):
    result, lst = [], []
    while node or lst:
        while node:
            lst.append(node)
            node = node.left
        node = lst.pop()
        result.append(node.data)
        node = node.right
    return result

# Post-order traversal
def post_order(node):
    if not node:
        return []
    lst1, lst2 = [node], []
    while lst1:
        node = lst1.pop()
        lst2.append(node)
        if node.left:
            lst1.append(node.left)
        if node.right:
            lst1.append(node.right)
    return [node.data for node in lst2[::-1]]
