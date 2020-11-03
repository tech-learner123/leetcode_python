class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # approach 1
        # nxt = [float('inf')] * 102
        # ans = [0] * len(T)
        # for i in range(len(T) - 1, -1, -1):
        #     #Use 102 so min(nxt[t]) has a default value
        #     warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
        #     if warmer_index < float('inf'):
        #         # compute the distance between the warmer index with the self
        #         ans[i] = warmer_index - i
        #     nxt[T[i]] = i
        # return ans

        # approach 2:
        # stack

        ans = [0] * len(T)

        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans