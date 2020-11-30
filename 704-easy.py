"""
binary search template
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if i == len(nums) or nums[i] != target:
            return -1