"""
Expand around the center
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # going one step back.
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            # odd case:
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case:
            tmp = helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res