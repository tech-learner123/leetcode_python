# instruction 
# https://www.youtube.com/watch?v=-rlQCg_TJac

class Solution:
    def numTrees(self, n: int) -> int:
        # tested results, recursive way TLE
        """
        if n <= 1:
            return 1
        count = 0
        for i in range(0, n):
            count += self.numTrees(i) * self.numTrees(n-i-1)
            print(i)
        return count

        """
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        # i is the number of value which is greater than n
        for i in range(2, n + 1):
            # j is the number of value which is less than i
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]