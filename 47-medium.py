from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # Approach1
        # def backtrack(first=0):
        #     if first == len(nums):
        ## for comparing purposes
        ##  output.append(nums[:])
        # if tuple(nums) not in seen:
        #     output.append(nums[:])
        #     seen.add(tuple(nums))
        #     for i in range(first, len(nums)):
        #         nums[first], nums[i] = nums[i], nums[first]
        #         backtrack(first + 1)
        #         nums[first], nums[i] = nums[i], nums[first]
        # output = []  
        # seen = set()
        # backtrack()
        # return output
        # approach 2: instead of swap, gradually add the number to avoid duplication. faster
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(comb[:])
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
