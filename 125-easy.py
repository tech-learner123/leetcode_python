class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            # Corner case: always keep in mind that i < j
            # alpha numerical
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            # Corner case, case insensitive
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True