class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # approach 1 iterative
        triangle = []
        for i in range(rowIndex + 1):
            temp = [1] * (i + 1)
            if i > 1:
                # skip the first and the last element
                for j in range(1, len(temp) - 1):
                    temp[j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
            triangle.append(temp)
        return temp
    # approach 2 recursive
        def helper(row_number):
            if row_number < 2:
                return [1]
            prev_row = helper(row_number - 1)
            temp = [1] * row_number
            for c in range(1, len(temp) - 1):
                temp[c] = prev_row[c - 1] + prev_row[c]
            return temp

        return helper(rowIndex + 1)

