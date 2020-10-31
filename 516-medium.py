class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(len(s) - 1, -1, -1):
            # corner case: 'a'
            dp[i][i] = 1
            for j in range(i + 1, len(s)):

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [1] * n
        for j in xrange(1, len(s)):
            pre = dp[j]
            for i in reversed(xrange(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]