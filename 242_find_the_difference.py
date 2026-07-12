def find_the_difference(s, t):
    res = 0
    for c in s + t:
        res ^= ord(c)
    return chr(res)

if __name__ == "__main__":
    print(find_the_difference("abcd", "abcde"))