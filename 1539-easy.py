class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maximum = max(arr)
        j = 0
        missing = 0

        for i in range(1, maximum + 1):
            if arr[j] == i:
                j += 1
            else:
                missing += 1
            if missing == k:
                return i
        # Edge cases:
        if missing < k:
            return (k - missing) + maximum