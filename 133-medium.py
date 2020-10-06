from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}
        queue = deque([node])
        # clone the node: based from the definition for a node.
        visited[node] = Node(node.val, [])
        while queue:
            sub_node = queue.popleft()
            for neighbor in sub_node.neighbors:
                # think: if not exits, then create a new node
                if neighbor not in visited:
                    # bfs
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # think: This part add the new nodes as neighbors to the subnode
                visited[sub_node].neighbors.append(visited[neighbor])

        return visited[node]