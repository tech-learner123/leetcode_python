class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            # first compaire the mid with the start value -> straight increasing order
            # [start, ..., mid, ..., end]
            if nums[mid] >= nums[start]:
                # second level check: compare the target value with the start and mid
                if target >= nums[start] and target < nums[mid]:  # [start, mid)
                    end = mid
                else:
                    start = mid + 1
            else:
                # not the straight increasing order the first half: e.g. [6, 7, 0, 1, 2, 4, 5]
                # (mid, end]
                # but is the straight increasing order for the second half
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid
        return -1
