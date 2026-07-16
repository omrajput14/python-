# 250. Island Perimeter
# Given a 2D grid map of 1s (land) and 0s (water),
# calculate the perimeter of the island.
# There is exactly one island with no lakes.

def island_perimeter(grid):
    """
    Each land cell contributes 4 to perimeter.
    Subtract 2 for each adjacent land cell (shared edge counted twice).
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                # Check top neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                # Check left neighbor
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter


# Example usage
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print("Grid:")
    for row in grid:
        print(row)
    print(f"Island perimeter: {island_perimeter(grid)}")
    # Output: 16
