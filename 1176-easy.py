class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # brute force approach
        total = 0
        point = 0
        for index in range(len(calories) - k + 1):
            # print(index)
            if index == 0:
                total = sum(calories[index: index + k])

            else:
                total = total - calories[index - 1] + calories[index + k - 1]
            # print(total)
            if total < lower:
                point -= 1
            elif total > upper:
                point += 1

        return point