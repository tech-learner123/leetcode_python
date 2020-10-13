# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        # approach 1. two pointers
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa

        """

        # approach 2: hash table
        if headA is None or headB is None:
            return None
        visited = set()

        while headA or headB:
            if headA != None:
                if headA not in visited:

                    visited.add(headA)
                else:
                    return headA
                headA = headA.next

            if headB != None:
                if headB not in visited:
                    visited.add(headB)
                else:
                    return headB
                headB = headB.next

