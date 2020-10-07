class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Think process:
        # The left element
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        # find the first element that is equal or larger than target
        print(left)

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        # find the first element that is larger than target
        print(left - 1)
        """

        def find_index(find_left):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (find_left and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left

        left_index = find_index(True)
        # do not exist a value in the list such that it equals to the target value.
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        # The first element that is larget than target.subtract by 1 is the value that == target.-> covered the corner cases: where such value exists.
        right_index = find_index(False) - 1
        return [left_index, right_index]
