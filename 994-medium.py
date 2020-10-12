from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs

        position = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs():
            while queue:
                cur_i, cur_j, step = queue.popleft()

                if grid[cur_i][cur_j] == 2:
                    for i, j in position:
                        new_i, new_j = cur_i + i, cur_j + j
                        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and (new_i, new_j) not in visited and \
                                grid[new_i][new_j] == 1:
                            queue.append((new_i, new_j, step + 1))
                            grid[new_i][new_j] = 2
                            visited.add((new_i, new_j))
            return step

        visited = set()
        queue = deque()
        step = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        # Corner case: if the queue does not exist:
        if queue:
            step = bfs()

        if any(grid[i][j] == 1 for j in range(len(grid[0])) for i in range(len(grid))):
            return -1
        else:
            return step




