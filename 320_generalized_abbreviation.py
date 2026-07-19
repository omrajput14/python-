# 320. Generalized Abbreviation
# A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings and replacing them with their respective lengths.

def generate_abbreviations(word):
    ans = []
    def backtrack(pos, cur, count):
        if pos == len(word):
            ans.append(cur + (str(count) if count > 0 else ""))
            return
        backtrack(pos + 1, cur, count + 1)
        backtrack(pos + 1, cur + (str(count) if count > 0 else "") + word[pos], 0)
    backtrack(0, "", 0)
    return ans

if __name__ == "__main__":
    print(generate_abbreviations("word"))
