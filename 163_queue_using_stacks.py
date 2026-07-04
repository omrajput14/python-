class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print("Peek:", queue.peek())  # returns 1
    print("Pop:", queue.pop())   # returns 1
    print("Empty?", queue.empty()) # returns False
