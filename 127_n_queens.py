def print_solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        print_solution(board)
        return True
    
    res = False
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            res = solve_n_queens_util(board, row + 1, n) or res
            board[row] = -1
    return res

def solve_n_queens(n):
    board = [-1] * n
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False
    return True

if __name__ == "__main__":
    solve_n_queens(4)
