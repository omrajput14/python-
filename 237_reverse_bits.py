def reverse_bits(n):
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res

if __name__ == "__main__":
    print(reverse_bits(43261596))