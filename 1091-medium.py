class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs

        r, c = len(grid), len(grid[0])
        # Corner case
        if not grid or grid[0][0] != 0 or grid[r - 1][c - 1] != 0:
            return -1
        queue = deque([(0, 0, 0)])

        seen = set()
        seen.add((0, 0))
        minimum = float(inf)
        # moving from topleft to bottom-right
        position = [(0, 1), (0, -1), (-1, 0), (-1, -1), (1, 0), (-1, 1), (1, -1), (1, 1)]
        while queue:
            cur_r, cur_c, step = queue.popleft()
            for delta_r, delta_c in position:
                new_r = cur_r + delta_r
                new_c = cur_c + delta_c

                if new_r == r and new_c == c:
                    minimum = min(minimum, step + 1)
                if 0 <= new_r < r and 0 <= new_c < c and (new_r, new_c) not in seen and grid[new_r][new_c] == 0:
                    queue.append((new_r, new_c, step + 1))
                    seen.add((new_r, new_c))
        return minimum if minimum != float(inf) else -1