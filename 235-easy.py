# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #         parent_val = root.val
        #         p_val = p.val
        #         q_val = q.val
        #         if p_val > parent_val and q_val > parent_val:
        #             return self.lowestCommonAncestor(root.right, p, q)
        #         elif p_val < parent_val and q_val <parent_val:
        #             return self.lowestCommonAncestor(root.left, p, q)
        #         else:
        #             return root

        # don't use stack
        node = root
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node

# general solution
#         parent = {root: None}
#         stack = [root]
#         while p not in parent or q not in parent:
#             node = stack.pop()
#             if root.left:
#                 parent[root.left] = root
#                 stack.append(root.left)
#             if root.right:
#                 parent[root.right] = root
#                 stack.append(root.right)
#         ancestor = set()
#         while p:
#             ancestor.add(p.val)
#             p = parent[p]

#         while q not in ancestor:
#             q = parent[q]

#         return q
