# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Searching space [1, n+1)
        left, right = 1, n + 1
        while left < right:
            mid = (left + right) // 2
            # g(m)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        # the first element that satisfy the function g(m)
        return left