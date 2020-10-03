class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        # Use the trie data structure:
        # Step 1: build the trie
        trie = {}
        for word in dictionary:
            node = trie
            for l in word:
                if l not in node:
                    node[l] = {}
                node = node[l]
            node['$'] = True

        # Search through the tree
        def check_if_word_in_trie(word, trie):
            node = trie
            replace_word = ''

            for l in word:
                if '$' in node:
                    return replace_word
                if l not in node:
                    return False
                else:
                    replace_word += l
                    node = node[l]

        ret = []
        for word in sentence.split(' '):
            replace_word = check_if_word_in_trie(word, trie)
            if not replace_word:
                ret.append(word)
            else:
                ret.append(replace_word)
        return ' '.join(ret)