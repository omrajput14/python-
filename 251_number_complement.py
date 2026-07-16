# 251. Number Complement
# Given a positive integer, output its complement number.
# The complement flips all bits in its binary representation.

def find_complement(num):
    """
    Find complement by creating a mask of all 1s with the same bit length.
    XOR with mask flips all bits.
    """
    if num == 0:
        return 1
    
    # Find the number of bits
    bit_length = num.bit_length()
    # Create mask with all 1s of same length
    mask = (1 << bit_length) - 1
    
    return num ^ mask


def find_complement_iterative(num):
    """Alternative: build complement bit by bit."""
    if num == 0:
        return 1
    
    result = 0
    power = 1
    
    while num > 0:
        # Flip the last bit and add to result
        result += (1 - (num & 1)) * power
        num >>= 1
        power <<= 1
    
    return result


# Example usage
if __name__ == "__main__":
    print(f"Complement of 5 (101): {find_complement(5)}")
    # 5 = 101, complement = 010 = 2

    print(f"Complement of 1 (1): {find_complement(1)}")
    # 1 = 1, complement = 0 = 0

    print(f"Complement of 7 (111): {find_complement(7)}")
    # 7 = 111, complement = 000 = 0

    print(f"\nIterative - Complement of 5: {find_complement_iterative(5)}")
    print(f"Iterative - Complement of 10: {find_complement_iterative(10)}")
    # 10 = 1010, complement = 0101 = 5
