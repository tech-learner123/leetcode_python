# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # [1,[2,4,5],[3,6,7] -> (root node) (preorder of left branch) (preorder of right branch)
        # [[4,5,2],[6,7,3],1] -> (postorder of left branch) (postorder of right branch) (root node)

        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        # the left index pre[1]
        # find the index of the element pre[1]
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return root