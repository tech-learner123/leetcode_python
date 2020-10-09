class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return True
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py

            else:
                parent[py] = px
                rank[px] += 1

        # when we have words instead of the int, use other format.
        parent = [i for i in range(len(pairs))]
        rank = [0] * len(pairs)

        word_to_index = dict()
        # build the graph
        for index, pair in enumerate(pairs):
            for word in pair:
                if word not in word_to_index:
                    word_to_index[word] = index
            union(parent[word_to_index[pair[0]]], parent[word_to_index[pair[1]]])

        for word1, word2 in zip(words1, words2):
            # don't miss the find step.
            if not (word1 == word2 or (
                    word1 in word_to_index and word2 in word_to_index and find(parent[word_to_index[word1]]) == find(
                    parent[
                        word_to_index[word2]]))):
                return False
        return True