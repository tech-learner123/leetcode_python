class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Edge cases: when k<=1, because nums[i] > 0
        if k <= 1:
            return 0
        product = 1
        left = 0
        ans = 0
        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product /= nums[left]
                left += 1
            ans += right - left + 1
        return ans