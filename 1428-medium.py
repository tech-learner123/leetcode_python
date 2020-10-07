# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        """
        approach 1:
        rows, columns = binaryMatrix.dimensions()
        min_columns = float(inf)
        def check_index(current_row, min_column):
            left, right = 0, columns
            while left < right:
                mid = (left + right) // 2

                if binaryMatrix.get(current_row, mid) == 1:
                    right = mid
                else:
                    left = mid + 1
            return left


        for r in range(rows):
            ret = check_index(r, min_columns)
            # Edge cases: where the no 1 exists for the row.
            if ret != columns and binaryMatrix.get(r, ret) == 1:
                min_columns = min(min_columns, ret)


        return min_columns if min_columns != float(inf) else -1

        """
        # approach 2: optimization
        rows, cols = binaryMatrix.dimensions()
        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1