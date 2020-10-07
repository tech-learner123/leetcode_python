import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles) + 1

        def compute_eating_time(speed):
            total_hours = 0
            for numbers in piles:
                if numbers <= speed:
                    total_hours += 1
                else:
                    total_hours += math.ceil(numbers / speed)
            return total_hours

        while left < right:
            mid = (left + right) // 2
            hour_spend = compute_eating_time(mid)
            if hour_spend <= H:
                right = mid
            else:
                left = mid + 1
        # the minimum value that satisfy this contition.
        return left
