# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(node_left, node_right):
            if node_left is None and node_right is None:
                return True
            if node_left is None or node_right is None:
                return False
            if node_left.val == node_right.val:
                outpair = helper(node_left.left, node_right.right)
                inpair = helper(node_left.right, node_right.left)
                return outpair and inpair
            else:
                return False

        if not root:
            return True
        return helper(root.left, root.right)



