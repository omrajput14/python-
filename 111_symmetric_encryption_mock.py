# Symmetric Encryption Mock (XOR Cipher) Example
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

if __name__ == "__main__":
    original = "Secret Message"
    key = "key"
    
    encrypted = xor_encrypt_decrypt(original, key)
    print(f"Encrypted: {repr(encrypted)}")
    
    decrypted = xor_encrypt_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
