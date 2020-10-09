class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        r, n, l = len(A), len(A[0]), len(B[0])
        # Don't need to consider this corner case as the question states that a's column number is equal to b's row number
        # if len(B) != n:
        #     raise Exception("A's column number must be equal to B's row number.")
        # Initial dense C matrix
        C = [[0 for _ in range(l)] for _ in range(r)]
        # https://machinelearningmastery.com/sparse-matrices-for-machine-learning/
        tableB = {}
        # convert the dense matrix into sparse matrix b,
        # k: the row number
        for k, row in enumerate(B):
            tableB[k] = {}
            # j the column number, eleb: the actual value of the cell
            for j, eleB in enumerate(row):
                if eleB: tableB[k][j] = eleB
        # Start matrix multiplication.
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                # if element is nonzero
                if eleA:
                    # Important.
                    for j, eleB in tableB[k].items():
                        C[i][j] += eleA * eleB
        return C
