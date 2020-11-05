from collections import Counter
"""
Summary backtracking 40 41 46, 47 permutation vs combination.
"""
# # approach 1
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         count = Counter(candidates)
#         tmp = []
#         res = []
#
#         def backtrack(cumulative):
#
#             if cumulative == target and sorted(tmp[:]) not in res:
#                 res.append(sorted(tmp[:]))
#                 return
#             elif cumulative > target:
#                 return
#
#             for candidate in count:
#                 if count[candidate] > 0:
#                     tmp.append(candidate)
#                     count[candidate] -= 1
#                     backtrack(cumulative + candidate)
#                     count[candidate] += 1
#                     tmp.pop()
#
#         backtrack(0)
#         return res

from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # optimization, remove the duplication
        candidates = sorted(candidates)

        def backtrack(index, cum):
            if cum == target:
                res.append(tmp[:])
            elif cum > target:
                return -1

            for i in range(index, len(candidates)):
                # Remove duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                tmp.append(candidates[i])
                # optimization: if the current number is already greater than target, break back to the previous loop
                flag = backtrack(i + 1, candidates[i] + cum)
                tmp.pop()
                if flag == -1:
                    break

        res = []
        tmp = []
        backtrack(0, 0)
        return res