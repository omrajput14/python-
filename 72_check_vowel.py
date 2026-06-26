# Check if a character is a vowel or consonant
def check_vowel_consonant(char):
    if char.lower() in 'aeiou':
        return "Vowel"
    elif char.isalpha():
        return "Consonant"
    else:
        return "Not an alphabet"

char1 = 'A'
char2 = 'b'

print(f"'{char1}' is a {check_vowel_consonant(char1)}")
print(f"'{char2}' is a {check_vowel_consonant(char2)}")
