# 291. Word Pattern II
# Given a pattern and a string s, return true if s matches the pattern.

def word_pattern_match(pattern, s):
    mapping = {}
    def backtrack(p_idx, s_idx):
        if p_idx == len(pattern) and s_idx == len(s): return True
        if p_idx == len(pattern) or s_idx == len(s): return False
        
        char = pattern[p_idx]
        if char in mapping:
            word = mapping[char]
            if not s.startswith(word, s_idx):
                return False
            return backtrack(p_idx + 1, s_idx + len(word))
        
        for i in range(s_idx + 1, len(s) + 1):
            word = s[s_idx:i]
            if word not in mapping.values():
                mapping[char] = word
                if backtrack(p_idx + 1, i): return True
                del mapping[char]
        return False
    return backtrack(0, 0)

if __name__ == "__main__":
    print(word_pattern_match("abab", "redblueredblue"))
