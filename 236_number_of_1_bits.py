def hamming_weight(n):
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res

if __name__ == "__main__":
    print(hamming_weight(11))