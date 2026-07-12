def is_power_of_three(n):
    if n < 1: return False
    while n % 3 == 0: n //= 3
    return n == 1

if __name__ == "__main__":
    print(is_power_of_three(27))