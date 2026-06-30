class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        i = 0
        length = len(matrix[0])
        j = len(matrix) * len(matrix[0]) - 1
        while i <= j:
            p = (i + j) // 2
            row = p // length
            col = p % length
            num = matrix[row][col]
            if num == target:
                return True
            if num < target:
                i = p + 1
            elif num > target:
                j = p - 1
        return False