from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remain, comb, start):

            if remain == 0:
                # make a deep copy of the current combination?
                result.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)
        return result


Solution().combinationSum([2,3,6,7], 7)
