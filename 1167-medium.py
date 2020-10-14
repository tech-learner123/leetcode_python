class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # corner case, if there is only one stick
        # this is wring because the intermediate results could be the minimum value. 
        # use heap
        """
         if len(sticks) < 2:
            return 0
        sort_stick = sorted(sticks)
        cost = 0
        total_length = len(sort_stick)
        print(sort_stick)
        for i in range(1, total_length):
            cost += sort_stick[total_length - i] * i
        cost += sort_stick[0] * (total_length - 1)

        return cost
        """

        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            cost += (x + y)
            # heap push the x+ y not hte cost
            heapq.heappush(sticks, x + y)
        return cost