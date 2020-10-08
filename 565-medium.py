class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        TLE: way too complicated.
        if len(nums) == 1:
            return 1
        index_map = {index: n for index, n in enumerate(nums)}
        visited = set()
        max_layer = 0
        def helper(item, layer):
            nonlocal max_layer
            max_layer = max(max_layer, layer)

            if item in index_map and item not in visited:
                visited.add(item)
                helper(index_map[item], layer + 1)

        for i in range(len(nums)):
            visited = set([i])
            helper(index_map[i], 1)
        return max_layer
        """

        seen, res = [0] * len(nums), 0
        for i in nums:
            cnt = 0
            while not seen[i]:
                seen[i], cnt, i = 1, cnt + 1, nums[i]
            res = max(res, cnt)
        return res

