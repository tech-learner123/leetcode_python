class Solution:
    def myPow(self, x: float, n: int) -> float:
        # approach 1: brute force approach. TLE
        """
         res = 1
        sign = 1
        if n == 0:
            return 1
        if n < 0:
            sign = -1
            n = n*sign
        while n > 0:
            res *= x
            n -= 1
        return res if sign > 0 else 1/res
        """

        # 2 (1) * 2 (1)  = 4 (2) * 4 (2)-> 16

        if n < 0:
            return 1 / self.helper(x, -n)
        else:
            return self.helper(x, n)

    def helper(self, a, b):
        if b == 0: return 1
        half = self.helper(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a

