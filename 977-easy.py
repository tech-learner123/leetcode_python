class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # approach 1: two pointers
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i] ** 2 < A[j] ** 2:
                ans.append(A[i] ** 2)
                i -= 1
            else:
                ans.append(A[j] ** 2)
                j += 1

        while i >= 0:
            ans.append(A[i] ** 2)
            i -= 1
        while j < N:
            ans.append(A[j] ** 2)
            j += 1

        return ans

        # approach 2: sorted
        # return sorted(x*x for x in A)