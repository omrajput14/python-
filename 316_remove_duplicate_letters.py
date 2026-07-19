# 316. Remove Duplicate Letters
# Given a string s, remove duplicate letters so that every letter appears once and only once.

def remove_duplicate_letters(s):
    last_occ = {c: i for i, c in enumerate(s)}
    stack = []
    seen = set()
    
    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
    return "".join(stack)

if __name__ == "__main__":
    print(remove_duplicate_letters("bcabc"))
