# 271. Reshape the Matrix
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
        
    flat = [item for row in mat for item in row]
    return [flat[i*c:(i+1)*c] for i in range(r)]

if __name__ == "__main__":
    print(matrix_reshape([[1,2],[3,4]], 1, 4))  # [[1, 2, 3, 4]]
    print(matrix_reshape([[1,2],[3,4]], 2, 4))  # [[1, 2], [3, 4]]
