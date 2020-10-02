# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Think: Leveraging the property of the binary search Tree,
# If node.val falls outside the range [L, R], (for example node.val < L),
# then we know that only the right branch could have nodes with value inside [L, R]
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val < L:
                    stack.append(node.right)
                elif node.val >= L and node.val <= R:
                    ans += node.val
                    stack.extend([node.left, node.right])
                elif node.val > R:
                    stack.append(node.left)
        return ans