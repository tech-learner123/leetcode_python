class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # here j indicate the next non duplicate position.
        j = 0
        mapping = {}
        length = 0
        for start, letter in enumerate(s):
            if letter in mapping and mapping[letter] + 1 > j:
                j = mapping[letter] + 1
            mapping[letter] = start
            length = max(length, start - j + 1)
        return length
