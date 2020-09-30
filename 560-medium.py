class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = {0: 1}
        current_sum = 0
        count = 0
        # order matters: first check if the residual exist or not -> add to the hashmap
        for n in nums:
            current_sum += n
            residual = current_sum - k
            if residual in prefix_sum:
                count += prefix_sum[residual]
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1

        return count
