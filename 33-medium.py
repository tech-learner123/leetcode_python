class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:  # [start, mid)
                    end = mid
                else:
                    start = mid + 1
            else:
                # (mid, end]
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid
        return -1
