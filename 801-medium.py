class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:

        keep, swap = [float(inf)] * len(A), [float(inf)] * len(A)
        keep[0] = 0
        swap[0] = 1
        for i in range(1, len(A)):
            # if both a and b follow restrict increasing,
            # we could either swap a[i] <-> b[i] and a[i-1] <-> b[i-1], or keep 
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1

            # if a and b crossed
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                # we could either swap the a[i-1] <-> b[i-1]
                keep[i] = min(keep[i], swap[i - 1])
                # or we swap the current step, keep the previous step keep[i-1] + 1
                swap[i] = min(swap[i], keep[i - 1] + 1)

        return min(swap[-1], keep[-1])


