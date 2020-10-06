from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # node coloring
        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            # traverse through the graph_map
            for v in graph[node]:
                # differenct color
                if dfs(v, c ^ 1) == False:
                    return False
            return True

        for index in range(len(graph)):
            if index not in color:
                if dfs(index) == False:
                    return False
        return True

