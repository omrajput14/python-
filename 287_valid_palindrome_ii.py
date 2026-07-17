# 287. Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def valid_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True

if __name__ == "__main__":
    print(valid_palindrome("aba"))   # True
    print(valid_palindrome("abca"))  # True
    print(valid_palindrome("abc"))   # False
