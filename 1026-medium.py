# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Three approaches to do this.
# the morris traversal approach:
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# discuss/702291/Python-Iterative-Recursive-and-Morris-Traversal-or-O(1)-space-and-O(n)-time-complexity

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res
