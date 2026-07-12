def first_uniq_char(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

if __name__ == "__main__":
    print(first_uniq_char("leetcode"))