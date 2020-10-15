# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def helper(root):
            if not root: return [0, 0.0]
            n1, s1 = helper(root.left)
            n2, s2 = helper(root.right)
            n = n1 + n2 + 1
            s = s1 + s2 + root.val
            self.res = max(self.res, s / n)
            return [n, s]

        self.res = 0
        helper(root)
        return self.res