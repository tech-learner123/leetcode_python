import random


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # Binary Search
        target = self.total_sum * random.random()
        # First: left close, right open
        start, end = 0, len(self.prefix_sums)
        while start < end:
            mid = (start + end) // 2

            # g(m): a statement [1,2,3]  2
            # find the first element that is greater or equal than the target.
            if self.prefix_sums[mid] >= target:
                end = mid
            else:
                start = mid + 1
        # Second, looking for the first element that satisfy the g(m) return j
        return start

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()