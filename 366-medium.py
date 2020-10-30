# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def helper(node):
            if not node:
                return -1
            left = helper(node.left)
            right = helper(node.right)
            level = max(left, right) + 1
            res[level].append(node.val)
            return level

        if not root:
            return []
        res = defaultdict(list)
        helper(root)

        return [res[i] for i in res.keys()]

