# Valid Parentheses Example
def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack

if __name__ == "__main__":
    expressions = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for expr in expressions:
        print(f"{expr}: {is_valid_parentheses(expr)}")
