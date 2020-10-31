from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs
        if not grid or not grid[0]:
            return 0

        queue = deque()
        count = 0
        row, col = len(grid), len(grid[0])

        def helper(i, j):
            # during this process search through all the connected islands and mark visited
            while queue:
                r, c = queue.popleft()
                if (r + 1) < row and grid[r + 1][c] == '1':
                    grid[r + 1][c] = '$'
                    queue.append((r + 1, c))
                if 0 <= r - 1 < row and grid[r - 1][c] == '1':
                    grid[r - 1][c] = '$'
                    queue.append((r - 1, c))
                if c + 1 < col and grid[r][c + 1] == '1':
                    grid[r][c + 1] = '$'
                    queue.append((r, c + 1))
                if 0 <= c - 1 < col and grid[r][c - 1] == '1':
                    grid[r][c - 1] = '$'
                    queue.append((r, c - 1))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    queue.append((i, j))
                    helper(i, j)
                    count += 1
        return count
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helper(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = '*'
                helper(i + 1, j)
                helper(i - 1, j)
                helper(i, j+1)
                helper(i, j-1)
    
        
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    helper(i, j)
                    count += 1
        return count
"""