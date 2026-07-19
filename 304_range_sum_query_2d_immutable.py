# 304. Range Sum Query 2D - Immutable
# Given a 2D matrix matrix, handle multiple queries of the following type:
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]: return
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r+1][c+1] = self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c] + matrix[r][c]

    def sum_region(self, row1, col1, row2, col2):
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]

if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    nm = NumMatrix(matrix)
    print(nm.sum_region(2, 1, 4, 3))
