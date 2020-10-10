class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """

        The above observation applies to our problem here as well.
        Given KK number of cells, there could be at most 2^K2 K possible states.
        If the number of steps is larger than all possible states (i.e. N \gt 2^KN>2K),
        we are destined to repeat ourselves sooner or later.

        """
        seen = dict()
        is_fast_forwarded = False
        while N > 0:
            # from the N count down to 0
            if not is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - N > 0

                    N %= seen[state_key] - N
                    is_fast_forwarded = True
                else:
                    seen[state_key] = N
            if N > 0:
                N -= 1
                next_day_cells = self.nextDay(cells)
                cells = next_day_cells
        return cells

    def nextDay(self, cells):
        # head
        ret = [0]
        for i in range(1, len(cells) - 1):
            ret.append(int(cells[i - 1] == cells[i + 1]))
        # tail
        ret.append(0)
        return ret