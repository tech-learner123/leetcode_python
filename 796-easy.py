class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # KMP
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        #Compute shift table
        # the largest prefix of B that ends here
        shifts = [1] * (N+1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1
        #print(shifts)
        # e.g. for "cbcbe" -> [1, 1,2,2,2,5]
        #Find match of B in A+A
        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False