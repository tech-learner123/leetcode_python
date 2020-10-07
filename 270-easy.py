# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        smallest = float(inf)
        closest = root.val

        def dfs(node):
            nonlocal smallest
            nonlocal closest
            if node:
                if abs(target - node.val) < smallest:
                    smallest = abs(target - node.val)
                    closest = node.val

            if node.val > target:
                if node.left:
                    dfs(node.left)
            else:
                if node.right:
                    dfs(node.right)

        dfs(root)
        return closest

