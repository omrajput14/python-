class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        # i is 1-based index
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        # i is 1-based index
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    ft = FenwickTree(len(arr))
    
    for i, val in enumerate(arr):
        ft.update(i + 1, val)
        
    print("Sum of first 3 elements:", ft.query(3))
    print("Sum from index 2 to 5 (1-based index):", ft.range_query(2, 5))
    
    print("Updating index 3 by adding 2")
    ft.update(3, 2)
    print("Sum from index 2 to 5 after update:", ft.range_query(2, 5))
