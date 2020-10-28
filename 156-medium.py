# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:

        if not root or not root.left:
            return root
        # traverse to the bottom left leaf as the new root
        lroot = self.upsideDownBinaryTree(root.left)
        # the new root
        rmost = lroot
        # traverse to the new root's new right as the next level root
        while rmost.right:
            rmost = rmost.right
        root, rmost.left, rmost.right = lroot, root.right, TreeNode(root.val)
        # return the current updated root
        return root