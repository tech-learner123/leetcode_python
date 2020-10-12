from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return rooms
        queue = deque([])
        visited = set()
        # store the inital points: gates
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        location = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            cur_r, cur_c, step = queue.popleft()
            for r, c in location:
                new_r, new_c = r + cur_r, c + cur_c
                # Nearest gate
                if 0 <= new_r < len(rooms) and 0 <= new_c < len(rooms[0]) and (
                        (new_r, new_c) not in visited and rooms[new_r][new_c] == 'INF' or rooms[new_r][
                    new_c] > step + 1):
                    rooms[new_r][new_c] = step + 1
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, step + 1))

        return rooms


