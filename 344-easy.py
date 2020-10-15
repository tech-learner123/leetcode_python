class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        start, end = 0, len(s) - 1

        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
"""
recursive approach
 def recursive(i, j):
            if i > j:
                return
            s[i], s[j] = s[j], s[i]
            return recursive(i+1, j-1)
        recursive(0, len(s) - 1)

"""