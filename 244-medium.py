from collections import defaultdict


class WordDistance:

    def __init__(self, words: List[str]):
        self.index_map = defaultdict(list)
        for index, word in enumerate(words):
            self.index_map[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        word_list1 = self.index_map[word1]
        word_list2 = self.index_map[word2]
        i, j, diff = 0, 0, float("inf")

        while i < len(word_list1) and j < len(word_list2):
            diff = min(diff, abs(word_list1[i] - word_list2[j]))
            if word_list1[i] < word_list2[j]:
                i += 1
            else:
                j += 1
        return diff

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)