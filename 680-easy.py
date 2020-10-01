class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Greedy approach.
        def is_par_or_not(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                # important it could go either way.
                return is_par_or_not(i, len(s) - 2 - i) or is_par_or_not(i + 1, len(s) - 1 - i)
        return True