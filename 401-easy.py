from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins > 59:
                return
            if not n:
                # edge cases: if min < 10 pad with 0
                res.append(str(hours) + ':'  "0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10):
                # Iterating through hours.
                if i < 4:
                    # hours | (1 << i) -> hours + (1 << i)
                    # bit manipulation: (1 << i) left shift 1 for ith position.
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                # Iterating through minites.
                else:
                    k = i - 4
                    # bit manipulation: (1 << k) left shift 1 for kth position.
                    dfs(n - 1, hours, mins | (1 << k), i + 1)

        res = []
        dfs(num, 0, 0, 0)
        return res


test = Solution()
test.readBinaryWatch(2)
