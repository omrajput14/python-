# 260. Longest Uncommon Subsequence I
# Given two strings a and b, return the length of the longest uncommon subsequence between a and b.

def find_lu_slength(a, b):
    if a == b:
        return -1
    return max(len(a), len(b))

if __name__ == "__main__":
    print(find_lu_slength("aba", "cdc"))  # 3
    print(find_lu_slength("aaa", "bbb"))  # 3
    print(find_lu_slength("aaa", "aaa"))  # -1
