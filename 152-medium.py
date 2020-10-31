class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # initial the first step
        prev_max, prev_min, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            prev_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
            # need this step don't want to update prev_max too soon line 9
            prev_max = temp
            res = max(res, prev_max)
        return res