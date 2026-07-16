# 255. Keyboard Row
# Given an array of strings, return the words that can be
# typed using letters of only one row on a QWERTY keyboard.

def find_words(words):
    """
    Check if all characters of a word belong to the same keyboard row.
    """
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = []
    for word in words:
        lower_word = set(word.lower())
        if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
            result.append(word)

    return result


# Example usage
if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(f"Words: {words}")
    print(f"Keyboard row words: {find_words(words)}")
    # Output: ["Alaska", "Dad"]

    words2 = ["omk"]
    print(f"\nWords: {words2}")
    print(f"Keyboard row words: {find_words(words2)}")
    # Output: []

    words3 = ["adsdf", "sfd"]
    print(f"\nWords: {words3}")
    print(f"Keyboard row words: {find_words(words3)}")
    # Output: ["adsdf", "sfd"]
