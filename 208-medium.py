class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie  ={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for l in word:
            if l not in node:
                node[l] = {}
            node = node[l]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for l in word:
            if l in node:
                node = node[l]
            else:
                return False
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for l in prefix:
            if l in node:
                node = node[l]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)