# Extract file extension from a filename
import os

filename = "document.pdf"
extension = os.path.splitext(filename)[1]
print("File:", filename)
print("Extension:", extension)
