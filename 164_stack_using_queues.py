from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        sz = len(self.q)
        for i in range(sz - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print("Top:", stack.top())   # returns 2
    print("Pop:", stack.pop())   # returns 2
    print("Empty?", stack.empty()) # returns False
