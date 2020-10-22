class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        The straight forward idea is to take x % 60 = 60 - t % 60,
        which is valid for the most cases.
        But if t % 60 = 0, x % 60 = 0 instead of 60.

        One solution is to use x % 60 = (60 - t % 60) % 60,
        the other idea is to use x % 60 = (600 - t) % 60.
        Not sure which one is more straight forward.

        """
        devisible_map = dict()
        count = 0
        for i in time:
            # print(60-i%60)
            count += devisible_map.get((60 - i % 60) % 60, 0)
            devisible_map[i % 60] = devisible_map.get(i % 60, 0) + 1
            # print(devisible_map)

        return count

        # c = [0] * 60
        # res = 0
        # for t in time:
        #     res += c[-t % 60]
        #     c[t % 60] += 1
        # return res