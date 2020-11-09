from collections import Counter
"""
Three approaches:
1. hashmap, applied better when one of the list if super large
2. sort + two pointers
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res