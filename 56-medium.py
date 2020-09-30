class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        for interval in sort_intervals:
            # think: no merge intervals -> if merge not exist or end of previous merge is smaller than current start
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged