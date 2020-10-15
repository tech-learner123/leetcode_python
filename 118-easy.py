"""
class Solution:
# @return a list of lists of integers
def generate(self, numRows):
    lists = []
    for i in range(numRows):
        lists.append([1]*(i+1))
        if i>1 :
            for j in range(1,i):
                lists[i][j]=lists[i-1][j-1]+lists[i-1][j]
    return lists

"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        result = []

        for i in self.generate(numRows - 1):
            result.append(i)

        temp_row = result[-1]
        new_row = [1]

        for i in range(len(temp_row) - 1):
            new_row.append(temp_row[i] + temp_row[i + 1])
        new_row.append(1)

        result.append(new_row)

        return result