# Matrix Transposition with Zip Example
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("Original matrix:")
    for row in matrix:
        print(row)
        
    transposed = transpose(matrix)
    print("\nTransposed matrix:")
    for row in transposed:
        print(row)
