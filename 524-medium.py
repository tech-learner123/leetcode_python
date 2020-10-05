# Two pointer
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # sort by first the length of word, then by the lexicographical order.
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for l in s:
                if i < len(word) and word[i] == l:
                    i += 1
            if i == len(word):
                return word
        return ""