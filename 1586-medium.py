# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/submissions/detail/403590845/
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.res = []
        # self.next_idx = 0
        # self.prev_idx = -1
        self.index = -1
        self._leftmost(root)

    def hasNext(self) -> bool:
        # If there are element in the res list
        if (self.index + 1) < len(self.res):
            return True
        return len(self.stack) > 0

    def _leftmost(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # When there are element in the result list
        if not len(self.stack) > 0:
            return None
        if len(self.res) > (self.index + 1):
            self.index += 1
            return self.res[self.index]
        # When need to traverse the new element
        node = self.stack.pop()
        self.res.append(node.val)
        self.index += 1
        if node.right:
            self._leftmost(node.right)
        return node.val

    def hasPrev(self) -> bool:

        return 0 <= (self.index - 1) < len(self.res) and self.res

    def prev(self) -> int:
        if not self.hasPrev:
            return None
        self.index -= 1
        return self.res[self.index]