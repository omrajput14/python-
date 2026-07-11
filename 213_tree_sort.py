class Node:
    def __init__(self, item=0):
        self.key = item
        self.left, self.right = None, None

def insert(key, root):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(key, root.left)
    elif key > root.key:
        root.right = insert(key, root.right)
    return root

def storeSorted(root, arr, i):
    if root is not None:
        i = storeSorted(root.left, arr, i)
        arr[i] = root.key
        i += 1
        i = storeSorted(root.right, arr, i)
    return i

def treeSort(arr):
    root = None
    if len(arr) == 0:
        return
    root = insert(arr[0], root)
    for i in range(1, len(arr)):
        root = insert(arr[i], root)
    storeSorted(root, arr, 0)

if __name__ == "__main__":
    arr = [5, 4, 7, 2, 11]
    treeSort(arr)
    print("Tree Sort:", arr)
