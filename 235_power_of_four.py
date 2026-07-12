def is_power_of_four(n):
    return n > 0 and (n & (n-1)) == 0 and (n & 0x55555555) != 0

if __name__ == "__main__":
    print(is_power_of_four(16))