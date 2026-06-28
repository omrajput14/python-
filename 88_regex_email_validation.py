# Regular Expressions Example
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

emails = ["test@example.com", "invalid-email.com", "user.name@domain.co.uk"]

for email in emails:
    status = "Valid" if validate_email(email) else "Invalid"
    print(f"{email}: {status}")
