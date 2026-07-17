# 259. Detect Capital
# We define the usage of capitals in a word to be right when one of the following cases holds:
# 1. All letters in this word are capitals, like "USA".
# 2. All letters in this word are not capitals, like "leetcode".
# 3. Only the first letter in this word is capital, like "Google".

def detect_capital_use(word):
    return word.isupper() or word.islower() or word.istitle()

if __name__ == "__main__":
    print(detect_capital_use("USA"))      # True
    print(detect_capital_use("FlaG"))     # False
