class Solution:
    def fib(self, N: int) -> int:

        cache = {}

        def helper(n):
            if n in cache:
                return cache[n]
            if n < 2:
                cache[n] = n
            else:
                cache[n] = helper(n - 1) + helper(n - 2)
            return cache[n]

        return helper(N)