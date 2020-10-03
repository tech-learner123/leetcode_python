# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # There could be two situations :
        # 1. If the node has a right child, the successor is somewhere
        # lower in the tree, see red nodes on the Fig. below.
        # Otherwise, the successor is somewhere upper in the tree, see blue nodes on the Fig.
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        stack = []
        inorder = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            if stack:
                node = stack.pop()
                if inorder == p.val:
                    return node
                inorder = node.val
            root = node.right
        return None
