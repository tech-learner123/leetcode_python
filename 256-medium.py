class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Corner case: when the costs doesn;t exists
        if len(costs) == 0:
            return 0
        r_prev, g_prev, b_prev = 0, 0, 0
        for cost in costs:
            r, g, b = cost[0], cost[1], cost[2]
            r += min(g_prev, b_prev)
            g += min(r_prev, b_prev)
            b += min(r_prev, g_prev)
            r_prev = r
            g_prev = g
            b_prev = b
        return min(r, g, b)