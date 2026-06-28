# Context Manager Example
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Closing file {self.filename}")
            self.file.close()

if __name__ == "__main__":
    with ManagedFile('test_context.txt') as f:
        f.write('Hello, Context Manager!')
        print("Wrote to file")
