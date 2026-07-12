def add_strings(num1, num2):
    res = []
    carry = 0
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    while p1 >= 0 or p2 >= 0 or carry:
        x1 = int(num1[p1]) if p1 >= 0 else 0
        x2 = int(num2[p2]) if p2 >= 0 else 0
        value = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10
        res.append(str(value))
        p1 -= 1; p2 -= 1
    return "".join(res[::-1])

if __name__ == "__main__":
    print(add_strings("11", "123"))