from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        counter = Counter(nums)
        for num in counter:
            if k > 0 and num + k in counter:
                result += 1
            elif k == 0 and counter[num] > 1:
                result += 1
        return result