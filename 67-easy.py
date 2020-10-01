class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # bit manipulation
        # x ^ y -> bit addition
        # (x & y) << 1 -> carry one over. 
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x&y) << 1
            x, y = answer, carry
        return bin(x)[2:]