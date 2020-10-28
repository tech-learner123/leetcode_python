class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # use stack to keep the order.
        stack = []
        lower = -float("inf")
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True