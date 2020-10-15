class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # bfs or dfs
        if not image:
            return image

        def helper(r, c):
            nonlocal visited
            image[r][c] = newColor
            for new_r, new_c in position:
                if 0 <= (new_r + r) < len(image) and 0 <= (new_c + c) < len(image[0]) and (
                new_r + r, new_c + c) not in visited and image[new_r + r][new_c + c] == color:
                    visited.add((new_r + r, new_c + c))
                    helper(new_r + r, new_c + c)
            return

        position = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        color = image[sr][sc]
        visited = set((sr, sc))
        if color == newColor:
            return image

        helper(sr, sc)
        return image