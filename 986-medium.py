class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # read the question carefully,
        # 1. closed interval,
        # 2. pairwise disjoint, no overlap among the intervals
        # 3. sorted order
        # two pointer.
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            # remove the interval with the smallest endpoint
            if low <= high:
                ans.append([low, high])
            if A[i][1] < B[j][1]:
                i+=1
            else:
                j+= 1
        return ans