
# slight different compare with the shorted word distance ii
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -1
        minimum = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
            if words[i] == word2:
                index2 = i

            if index1 != -1 and index2 != -1:
                minimum = min(minimum, abs(index1 - index2))
        return minimum