from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先记录哪些行、列包含 0，再修改矩阵
        row_has_zero = [0 in row for row in matrix]  # 行是否包含 0
        col_has_zero = [0 in col for col in zip(*matrix)]  # 列是否包含 0

        for i, row0 in enumerate(row_has_zero):
            for j, col0 in enumerate(col_has_zero):
                if row0 or col0:  # i 行或 j 列有 0
                    matrix[i][j] = 0  # 题目要求原地修改，无返回值



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) #行数
        n = len(matrix[0]) #列数
        #第一行是否有0
        first_row = 0 in matrix[0]
        first_col = any(row[0] == 0 for row in matrix)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_col:
            for row in matrix:
                row[0] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0