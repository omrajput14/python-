class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
        
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
            
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(left_child, start, mid, idx, val)
            else:
                self.update(right_child, mid + 1, end, idx, val)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
            
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node + 1, start, mid, l, r)
        p2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return p1 + p2

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print("Sum of values in given range (1, 3):", st.query(0, 0, len(arr)-1, 1, 3))
    print("Updated array at index 1 to 10")
    st.update(0, 0, len(arr)-1, 1, 10)
    print("Sum of values in given range (1, 3):", st.query(0, 0, len(arr)-1, 1, 3))
