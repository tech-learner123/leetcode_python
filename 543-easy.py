# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Think: self.answer track the maximum number of node if closing the loop, while max(right, left) + 1 track number of node without closing the loop.

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 1

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, right + left + 1)

            return max(right, left) + 1

        depth(root)
        # The final answer subtract by 1 is get the path not the number of node.
        return self.ans - 1