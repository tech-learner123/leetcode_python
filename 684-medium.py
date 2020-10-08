class UnionFind(object):
    def __init__(self):
        # question: why 1001??? not 1000
        self.parent = [i for i in range(1001)]
        self.rank = [0] * 1001

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        # if the x and y are in the same cluster
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        find_edges = UnionFind()
        for edge in edges:
            # to check if the two vertices are connected before or not.
            if not find_edges.union(*edge):
                return edge