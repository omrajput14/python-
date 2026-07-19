# 311. Sparse Matrix Multiplication
# Given two sparse matrices mat1 and mat2, return the result of mat1 x mat2.

def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    ans = [[0] * n for _ in range(m)]
    for r in range(m):
        for i in range(k):
            if mat1[r][i] != 0:
                for c in range(n):
                    if mat2[i][c] != 0:
                        ans[r][c] += mat1[r][i] * mat2[i][c]
    return ans

if __name__ == "__main__":
    print(multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]]))
