"""
Summary: Union find.
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

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

        parent = [i for i in range(len(M))]
        rank = [0] * len(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    # if i and j are friends, union them together.
                    union(i, j)
        # Important find(i) need
        return len(set(find(i) for i in parent))