# 267. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverse_words(s):
    return " ".join(word[::-1] for word in s.split(" "))

if __name__ == "__main__":
    print(reverse_words("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"
    print(reverse_words("God Ding"))                     # "doG gniD"
