# 308. Range Sum Query 2D - Mutable
# Given a 2D matrix matrix, handle multiple queries of the following types: Update and Sum Region.

class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]: return
        self.matrix = matrix
        self.bit = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self._add(r, c, matrix[r][c])

    def _add(self, r, c, val):
        r += 1
        while r < len(self.bit):
            curr_c = c + 1
            while curr_c < len(self.bit[0]):
                self.bit[r][curr_c] += val
                curr_c += curr_c & -curr_c
            r += r & -r

    def update(self, row, col, val):
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._add(row, col, diff)

    def _sum(self, r, c):
        res = 0
        r += 1
        while r > 0:
            curr_c = c + 1
            while curr_c > 0:
                res += self.bit[r][curr_c]
                curr_c -= curr_c & -curr_c
            r -= r & -r
        return res

    def sum_region(self, row1, col1, row2, col2):
        return self._sum(row2, col2) - self._sum(row1 - 1, col2) - self._sum(row2, col1 - 1) + self._sum(row1 - 1, col1 - 1)

if __name__ == "__main__":
    nm = NumMatrix([[3,0,1,4,2],[5,6,3,2,1]])
    print(nm.sum_region(0,0,1,1))
