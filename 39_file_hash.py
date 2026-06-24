# Find Hash of File
import hashlib

def hash_file(filename):
   h = hashlib.sha1()
   with open(filename, 'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

message = hash_file("39_file_hash.py")
print("SHA-1 Hash of this file:", message)
