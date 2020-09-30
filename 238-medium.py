class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 1.
        # think: why use the 1 here because the integers where n > 1
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i -1]
        # optimize: use reversed(range(length - 1))
        # for i in reversed(range(length-1)):
        for i in range(len(nums) -2, -1, -1):
            right_product[i] = nums[i+ 1] * right_product[i+ 1]

        return [right_product[i] * left_product[i] for i in range(len(nums))]

        # Solution 2: optimize solution space optimize. constant space
        left_product = [1] * len(nums)

        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        r = 1
        for i in reversed(range(len(nums))):
            left_product[i] = left_product[i] * r
            r *= nums[i]
        return left_product