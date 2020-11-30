class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # approah 1: gauss formula
        # expected_sum = len(nums)*(len(nums)+1)//2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum
        # approach 2: hashset
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number