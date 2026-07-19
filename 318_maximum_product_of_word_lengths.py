# 318. Maximum Product of Word Lengths
# Given a string array words, return the maximum value of length(word[i]) * length(word[j]).

def max_product(words):
    masks = []
    lens = []
    for word in words:
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord('a'))
        masks.append(mask)
        lens.append(len(word))
        
    ans = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if masks[i] & masks[j] == 0:
                ans = max(ans, lens[i] * lens[j])
    return ans

if __name__ == "__main__":
    print(max_product(["abcw","baz","foo","bar","xtfn","abcdef"]))
