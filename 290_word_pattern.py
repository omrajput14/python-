# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            if word in word_to_char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char
            
    return True

if __name__ == "__main__":
    print(wordPattern("abba", "dog cat cat dog"))  # True
    print(wordPattern("abba", "dog cat cat fish")) # False
    print(wordPattern("aaaa", "dog cat cat dog"))  # False
    print(wordPattern("abba", "dog dog dog dog"))  # False
