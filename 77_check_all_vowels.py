# Check if a string contains all vowels
def contains_all_vowels(s):
    vowels = set("aeiou")
    return vowels.issubset(set(s.lower()))

string1 = "Education"
string2 = "Hello World"

print(f"'{string1}' contains all vowels:", contains_all_vowels(string1))
print(f"'{string2}' contains all vowels:", contains_all_vowels(string2))
