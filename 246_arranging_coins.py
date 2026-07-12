def arrange_coins(n):
    l, r = 0, n
    while l <= r:
        k = (r + l) // 2
        curr = k * (k + 1) // 2
        if curr == n: return k
        if n < curr: r = k - 1
        else: l = k + 1
    return r

if __name__ == "__main__":
    print(arrange_coins(5))