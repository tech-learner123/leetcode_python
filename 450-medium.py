# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
summary：
Two steps: 1. find the value 2. remove the value, 3. update the tree (option)
[1,2,3,4,]
if the removed point is the leaf node, no step 3
if the removed point is in the middle, need to update the tree
have two ways,
1. if the node has right node, fill the node with the right node successor
2. if the node has only left node, fill the node with the predecessor, going all the way to the right
"""


class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        # to Avoid having the None while root.left instead of while root
        # root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        # root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root.right)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)

        return root