# 253. Construct the Rectangle
# A web developer needs to know how to design a web page's size.
# Given area, find length L and width W such that:
# L * W = area, L >= W, and L - W is minimized.

import math


def construct_rectangle(area):
    """
    Start from the square root and work downward to find
    the closest factor pair that minimizes L - W.
    """
    w = int(math.sqrt(area))
    while area % w != 0:
        w -= 1
    return [area // w, w]


# Example usage
if __name__ == "__main__":
    print(f"Area 4: {construct_rectangle(4)}")
    # Output: [2, 2]

    print(f"Area 37: {construct_rectangle(37)}")
    # Output: [37, 1] (37 is prime)

    print(f"Area 122122: {construct_rectangle(122122)}")
    # Output: [427, 286]

    print(f"Area 100: {construct_rectangle(100)}")
    # Output: [10, 10]

    print(f"Area 24: {construct_rectangle(24)}")
    # Output: [6, 4]
