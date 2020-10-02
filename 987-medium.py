# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict


class Solution:
    # Three level of order
    # 1. column-wise order
    # 2. row-wise order
    # 3. value-wise order
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        min_column = max_column = 0

        def helper(root):
            # think: thie min_max column name is only used for tracking the range.
            nonlocal min_column, max_column

            queue = deque([(root, 0, 0)])
            while queue:
                node, row, column = queue.popleft()
                if node:
                    column_table[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        helper(root)
        ret = []
        for col in range(min_column, max_column + 1):
            ret.append([val for row, val in sorted(column_table[col])])
        return ret