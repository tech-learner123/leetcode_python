import random


class Solution:

    def __init__(self, nums: List[int]):
        self.numbers = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0
        # reservior sampling
        for index, n in enumerate(self.numbers):
            if n == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = index
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)