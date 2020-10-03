from collections import defaultdict


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # build the trie
        # nested dictionary data structure node -> node = {'d': {'o': {'g': {'$': True}}}}
        node = self.trie
        for l in word:
            if l not in node:
                node[l] = {}
            node = node[l]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('oath')
obj.addWord('dig')
param_2 = obj.search('.ig')