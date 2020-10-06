import collections


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # node coloring.
        graph = collections.defaultdict(list)
        # build the graph
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color = {}
        # dfs
        def dfs(node, c=0):
            if node in color:
                # check if the color is conflict
                return color[node] == c
            color[node] = c
            vertices = graph[node]
            for v in vertices:
                if dfs(v, c ^ 1) == False:
                    return False
            return True

        for node in range(1, N + 1):
            if node not in color:
                if dfs(node) == False:
                    return False
        return True