# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        parent = None
        curr = root
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not curr:
            return root
        if not curr.left:
            r = curr.right
        elif not curr.right:
            r = curr.left
        else:
            r = self.temp_func(curr)
            r.left = curr.left
        if not parent:
            return r
        if parent.left == curr:
            parent.left = r
        else:
            parent.right = r
        return root

    def temp_func(self, node):
        temp = node
        s = node.right
        while s.left:
            temp = s
            s = s.left

        if temp != node:
            temp.left = s.right
            s.right = node.right

        return s
