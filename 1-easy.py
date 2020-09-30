from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_map = defaultdict(list)

        for index, n in enumerate(nums):
            if n not in lookup_map:
                lookup_map[target - n].append(index)
            else:
                lookup_map[n].append(index)
                return lookup_map[n]
        return []