def is_perfect_square(num):
    r = num
    while r*r > num:
        r = (r + num//r) // 2
    return r*r == num

if __name__ == "__main__":
    print(is_perfect_square(16))