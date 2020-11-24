class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # n, m -> n, m+1, n, m+j
        # n+1, m+j
        # n+2, m+j
        # n+i, m+j
        # n+i, m+j-1
        # n+i, m+j-2
        # simulation
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in range(R)]
        ans = []
        # direction right, down, left, up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                # change the direction.
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
