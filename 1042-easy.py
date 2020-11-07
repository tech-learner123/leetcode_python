"""
Summary: greedy
"""

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Greedy approach.
        res = [0] * n
        # connected graph
        G = [[] for i in range(n)]
        # build the path
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        # print(G)
        for i in range(n):
            # remove a random item from the set: set.pop()
            # keep the left possible flower set(a) - set(b) and random select one from the remainder
            # {res[j] for j in G[i]} the current used flower, 0 no flower is used.
            # print({res[j] for j in G[i]})
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res