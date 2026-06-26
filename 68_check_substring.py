# Check if a string contains a substring
main_string = "The quick brown fox jumps over the lazy dog"
substring = "brown fox"

if substring in main_string:
    print(f"'{substring}' is present in the main string.")
else:
    print(f"'{substring}' is not present in the main string.")
