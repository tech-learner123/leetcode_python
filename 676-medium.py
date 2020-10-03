import collections
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + "*" + word[i + 1:]

    def buildDict(self, dictionary: List[str]) -> None:
        # convert the list to hashset
        self.words = set(dictionary)
        self.count = collections.Counter(nei for word in self.words for nei in self._genneighbors(word))

    def search(self, searchWord: str) -> bool:
        return any(self.count[nei] > 1 or (self.count[nei] == 1 and searchWord not in self.words) for nei in
                   self._genneighbors(searchWord))

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
