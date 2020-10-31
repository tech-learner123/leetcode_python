import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        # Brute force
        i, j = 0, 0
        heap = []
        res = []
        for n in nums1:
            for m in nums2:
                heapq.heappush(heap, (n+m, n, m))
        while k > 0 and heap:
            _, n, m = heapq.heappop(heap)
            res.append([n, m])
            k -= 1
        return res

        """
        if not nums1 or not nums2:
            return []
        # update the k

        ret = []
        res = [(nums1[0] + nums2[0], (0, 0))]
        visited = set()
        # dfs pop the minimum
        while len(ret) < k and res:
            _, (index1, index2) = heapq.heappop(res)
            ret.append((nums1[index1], nums2[index2]))
            if index1 + 1 < len(nums1) and (index1 + 1, index2) not in visited:
                heapq.heappush(res, (nums1[index1 + 1] + nums2[index2], [index1 + 1, index2]))
                visited.add((index1 + 1, index2))
            if index2 + 1 < len(nums2) and (index1, index2 + 1) not in visited:
                heapq.heappush(res, (nums1[index1] + nums2[index2 + 1], [index1, index2 + 1]))
                visited.add((index1, index2 + 1))
        return ret