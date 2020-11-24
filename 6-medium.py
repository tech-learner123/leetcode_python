class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        # iterating the rows.
        L = [''] * numRows
        index, step = 0, 1
        # change the direction by step:
        # positive step vs negative step
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)