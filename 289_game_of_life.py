# 289. Game of Life
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:
# 1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])
    
    # Define state transitions to do it in-place:
    # 0 -> 0: 0
    # 1 -> 1: 1
    # 1 -> 0: 2 (was alive, now dead)
    # 0 -> 1: 3 (was dead, now alive)
    
    def count_live_neighbors(r, c):
        live_count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (board[nr][nc] == 1 or board[nr][nc] == 2):
                    live_count += 1
        return live_count

    for r in range(m):
        for c in range(n):
            live_neighbors = count_live_neighbors(r, c)
            if board[r][c] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 2  # Dies
            elif board[r][c] == 0:
                if live_neighbors == 3:
                    board[r][c] = 3  # Becomes alive

    # Finalize the next state
    for r in range(m):
        for c in range(n):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == 3:
                board[r][c] = 1

if __name__ == "__main__":
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    print("Initial Board:")
    for row in board:
        print(row)
        
    gameOfLife(board)
    
    print("\\nNext State:")
    for row in board:
        print(row)
    # Output:
    # [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
