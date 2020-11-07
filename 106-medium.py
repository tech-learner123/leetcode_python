# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder left root right
        # postorder left right root

        def helper(left, right):
            if left == right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            index = index_map[root_val]
            # Need to put the right tree firstbuild right subtree
            root.right = helper(index + 1, right)
            # build left subtree
            root.left = helper(left, index)
            return root

        index_map = {v: i for i, v in enumerate(inorder)}
        return helper(0, len(inorder))
