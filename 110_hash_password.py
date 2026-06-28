# Hash Password Example
import hashlib
import os

def hash_password(password):
    salt = os.urandom(32)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + pwd_hash

def verify_password(stored_password, provided_password):
    salt = stored_password[:32]
    stored_hash = stored_password[32:]
    pwd_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwd_hash == stored_hash

if __name__ == "__main__":
    hashed = hash_password('super_secret')
    print("Password verification:", verify_password(hashed, 'super_secret'))
    print("Wrong password verification:", verify_password(hashed, 'wrong_secret'))
