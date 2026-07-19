# 302. Smallest Rectangle Enclosing Black Pixels
# You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

def min_area(image, x, y):
    top = min(r for r in range(len(image)) if '1' in image[r])
    bottom = max(r for r in range(len(image)) if '1' in image[r])
    left = min(c for c in range(len(image[0])) if any(image[r][c] == '1' for r in range(len(image))))
    right = max(c for c in range(len(image[0])) if any(image[r][c] == '1' for r in range(len(image))))
    return (bottom - top + 1) * (right - left + 1)

if __name__ == "__main__":
    image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]
    print(min_area(image, 0, 2))
