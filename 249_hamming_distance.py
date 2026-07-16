# 249. Hamming Distance
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.

def hamming_distance(x, y):
    """
    Calculate Hamming distance using XOR and bit counting.
    XOR gives 1 where bits differ, then count the 1s.
    """
    xor = x ^ y
    distance = 0
    while xor:
        distance += xor & 1
        xor >>= 1
    return distance


def hamming_distance_builtin(x, y):
    """Alternative using Python's built-in bin() and count()."""
    return bin(x ^ y).count('1')


def total_hamming_distance(nums):
    """
    Calculate total Hamming distance between all pairs in the array.
    For each bit position, count numbers with that bit set.
    Contribution = count_ones * count_zeros.
    """
    total = 0
    for bit in range(32):
        ones = sum(1 for num in nums if num & (1 << bit))
        zeros = len(nums) - ones
        total += ones * zeros
    return total


# Example usage
if __name__ == "__main__":
    print(f"Hamming distance(1, 4): {hamming_distance(1, 4)}")
    # 1 = 001, 4 = 100 -> distance = 2

    print(f"Hamming distance(3, 1): {hamming_distance(3, 1)}")
    # 3 = 11, 1 = 01 -> distance = 1

    print(f"Builtin method(1, 4): {hamming_distance_builtin(1, 4)}")

    nums = [4, 14, 2]
    print(f"\nTotal Hamming distance of {nums}: {total_hamming_distance(nums)}")
    # Output: 6
