# 264. Reverse String II
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

def reverse_str(s, k):
    a = list(s)
    for i in range(0, len(a), 2*k):
        a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)

if __name__ == "__main__":
    print(reverse_str("abcdefg", 2))  # "bacdfeg"
    print(reverse_str("abcd", 2))     # "bacd"
