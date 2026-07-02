def word_break(wordList, word):
    if word == '':
        return True
    
    wordLen = len(word)
    dp = [False] * (wordLen + 1)
    dp[0] = True

    for i in range(1, wordLen + 1):
        for j in range(i):
            if dp[j] and word[j:i] in wordList:
                dp[i] = True
                break

    return dp[wordLen]

if __name__ == '__main__':
    dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
    word = "ilikesamsung"
    if word_break(dictionary, word):
        print(f"'{word}' can be segmented")
    else:
        print(f"'{word}' cannot be segmented")
