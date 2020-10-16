# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        # iterative
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

        """
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        # n curr
        n = node.next
        node.next = prev
        return self._reverse(n, node)