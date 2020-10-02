# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right_side_node = []
        queue = deque([root])

        while queue:
            # think: This is important to get the number of total node per layer
            length_layer = len(queue)
            for i in range(length_layer):

                node = queue.popleft()
                # Iterating through the node within the same layer and retrieve the far right side of it.
                if i == length_layer - 1:
                    right_side_node.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_side_node
