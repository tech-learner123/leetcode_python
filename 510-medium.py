"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # If the node has right branch
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        # if node has parent and node is the right side of the parent
        while node.parent and node == node.parent.right:
            node = node.parent
        # If the node has a right child, and hence its successor is somewhere lower in the tree.
        # Go to the right once and then as many times to the left as you could. Return the node you end up with.
        # Node has no right child, and hence its successor is somewhere upper in the tree. Go up till the node that is left child of its parent.
        # The answer is the parent.
        return node.parent