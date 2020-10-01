class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
       # Still not quite clear. Want to compaire this one with the production.
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res