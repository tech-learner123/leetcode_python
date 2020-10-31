# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # edge cases
        self.ans = float("inf")
        if not root or not root.left:
            return -1
        smallest = root.val
        # Let \text{min1 = root.val}min1 = root.val. When traversing the tree at some node, \text{node}node, if \text{node.val > min1}node.val > min1, we know all values in the subtree at \text{node}node are at least \text{node.val}node.val, so there cannot be a better candidate for the second minimum in this subtree. Thus, we do not need to search this subtree.
        def dfs(node):
            if node:
                if smallest < node.val < self.ans:
                    self.ans = node.val
                elif node.val == smallest:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans < float('inf') else -1