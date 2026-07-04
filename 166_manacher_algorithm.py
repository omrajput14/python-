def find_longest_palindromic_substring(text):
    if not text:
        return ""
    
    T = '#'.join(f"^{text}$")
    n = len(T)
    P = [0] * n
    C = 0
    R = 0
    
    for i in range(1, n - 1):
        i_mirror = 2 * C - i
        
        if R > i:
            P[i] = min(R - i, P[i_mirror])
            
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
            
        if i + P[i] > R:
            C = i
            R = i + P[i]
            
    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_index = i
            
    start = (center_index - max_len) // 2
    return text[start: start + max_len]

if __name__ == '__main__':
    text = "babad"
    print(f"Original text: {text}")
    print(f"Longest Palindromic Substring: {find_longest_palindromic_substring(text)}")
    text2 = "cbbd"
    print(f"Original text: {text2}")
    print(f"Longest Palindromic Substring: {find_longest_palindromic_substring(text2)}")
