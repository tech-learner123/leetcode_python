# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(node=head):
            # swap the first and second element value
            if not node or node.next == None:
                return
            node.val, node.next.val = node.next.val, node.val
            return helper(node.next.next)

        helper()
        return head
