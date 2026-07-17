import os
import subprocess

directory = '/Users/0mrajput/Desktop/python'
os.chdir(directory)

files = {
    '211_tim_sort.py': '''MIN_MERGE = 32

def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size

if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19]
    timSort(arr)
    print("Tim Sort:", arr)
''',

    '212_shell_sort.py': '''def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]
    shellSort(arr)
    print("Shell Sort:", arr)
''',

    '213_tree_sort.py': '''class Node:
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
''',

    '214_bucket_sort.py': '''def bucketSort(arr):
    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])
    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)
    for i in range(slot_num):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

if __name__ == "__main__":
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Bucket Sort:", bucketSort(arr))
''',

    '215_pancake_sort_recursive.py': '''def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def findMax(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def pancakeSortRecursive(arr, n):
    if n <= 1:
        return
    mi = findMax(arr, n)
    if mi != n - 1:
        flip(arr, mi)
        flip(arr, n - 1)
    pancakeSortRecursive(arr, n - 1)

if __name__ == "__main__":
    arr = [23, 10, 20, 11, 12, 6, 7]
    pancakeSortRecursive(arr, len(arr))
    print("Pancake Sort Recursive:", arr)
'''
}

sorted_files = sorted(files.keys())

for filename in sorted_files:
    content = files[filename]
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Adding, committing, and pushing {filename}...")
    subprocess.run(['git', 'add', filename])
    subprocess.run(['git', 'commit', '-m', f"Add {filename} (algorithm)"])
    subprocess.run(['git', 'push'])

print("All 5 files pushed successfully!")
