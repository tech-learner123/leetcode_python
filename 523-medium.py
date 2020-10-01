class Solution:
    def checkSubarraySum(self, A, k):
        # setdefault(key[, default])
        # If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
        # default defaults to None.
        seen, cur = {0: -1}, 0
        for index, val in enumerate(A):
            # todo: why abs here.
            cur = (cur + val) % abs(k) if k else cur + val
            if index - seen.setdefault(cur, index) > 1:
                return True
        return False