# 301. Remove Invalid Parentheses
# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

def remove_invalid_parentheses(s):
    def is_valid(s):
        count = 0
        for char in s:
            if char == '(': count += 1
            if char == ')': count -= 1
            if count < 0: return False
        return count == 0

    level = {s}
    while True:
        valid = list(filter(is_valid, level))
        if valid: return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

if __name__ == "__main__":
    print(remove_invalid_parentheses("()())()"))
