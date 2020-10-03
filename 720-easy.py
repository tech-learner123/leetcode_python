class Solution:
    def longestWord(self, words: List[str]) -> str:
        # build the trie
        trie = {}
        longest = 0
        for index, word in enumerate(words):
            node = trie
            for l in word:
                if l not in node:
                    node[l] = {}
                node = node[l]
            # store the word in index to the end. 
            node['$'] = index

        # values
        stack = list(trie.values())
        print(trie)
        ans = ""
        # dfs
        while stack:
            cur = stack.pop()
            if '$' in cur:
                # read the index to the words
                word = words[cur['$']]
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != '$'])

        return ans

