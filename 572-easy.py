# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def is_match(s, t):
            if not (s and t):
                return s is t
            return (s.val == t.val
                    and is_match(s.left, t.left)
                    and is_match(s.right, t.right))

        if is_match(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)