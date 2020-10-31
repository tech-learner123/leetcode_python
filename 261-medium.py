class UnionFind:
    def __init__(self, n):
        self.parents = [n for n in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        rank_x, rank_y = self.rank[px], self.rank[py]
        if rank_x > rank_y:
            self.parents[py] = px
        elif rank_x < rank_y:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.rank[px] += 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # two approaches

        """
         # graph + iterative dfs
        adj_list = [[] for _ in range(n)]
        if len(edges) != n-1: return False
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        parent = {0:-1}
        stack = [0]

        while stack:
            node = stack.pop()
            for neig in adj_list[node]:
                if neig == parent[node]:
                    continue
                if neig in parent:
                    return False
                parent[neig] = node
                stack.append(neig)
        return len(parent) == n

        """
        # union find.
        if len(edges) != n - 1: return False
        case = UnionFind(n)
        for a, b in edges:
            if not case.union(a, b):
                return False
        return True