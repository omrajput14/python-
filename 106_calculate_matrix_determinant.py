# Calculate Matrix Determinant Example (2x2 and 3x3)
def determinant_2x2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def determinant_3x3(matrix):
    a = matrix[0][0] * determinant_2x2([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    b = matrix[0][1] * determinant_2x2([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    c = matrix[0][2] * determinant_2x2([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    return a - b + c

if __name__ == "__main__":
    m3x3 = [[6, 1, 1],
            [4, -2, 5],
            [2, 8, 7]]
    print("Determinant of 3x3 matrix:", determinant_3x3(m3x3))
