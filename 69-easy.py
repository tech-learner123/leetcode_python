class Solution:
    def mySqrt(self, x: int) -> int:
        # corner case
        if x < 2:
            return x
        left, right = 1, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1