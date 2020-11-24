class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # two pointers
        new_arr = [num % k for num in arr]
        # sort in place
        new_arr.sort()
        l, r = 0, len(arr) - 1
        while l <= r and new_arr[l] == 0:
            l += 1
        # edge cases
        if l % 2 == 1:
            return False
        while l < r:
            if new_arr[l] + new_arr[r] != k:
                return False
            l += 1
            r -= 1
        return True