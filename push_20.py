import os
import subprocess

directory = '/Users/0mrajput/Desktop/python'
os.chdir(directory)

files = {
    '191_linear_search.py': '''def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    print(linear_search([1,2,3], 2))''',
    
    '192_binary_search_iterative.py': '''def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == x: return m
        elif arr[m] < x: l = m + 1
        else: r = m - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1,2,3], 2))''',
    
    '193_jump_search.py': '''import math
def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n: return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n): return -1
    if arr[prev] == x: return prev
    return -1

if __name__ == "__main__":
    print(jump_search([1,2,3], 2))''',
    
    '194_interpolation_search.py': '''def interpolation_search(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x: return lo
            return -1
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] == x: return pos
        if arr[pos] < x: lo = pos + 1
        else: hi = pos - 1
    return -1

if __name__ == "__main__":
    print(interpolation_search([1,2,3], 2))''',
    
    '195_exponential_search.py': '''def binary_search(arr, l, r, x):
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == x: return m
        if arr[m] < x: l = m + 1
        else: r = m - 1
    return -1

def exponential_search(arr, x):
    if arr[0] == x: return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2, min(i, n-1), x)

if __name__ == "__main__":
    print(exponential_search([1,2,3], 2))''',
    
    '196_ternary_search.py': '''def ternary_search(l, r, key, arr):
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == key: return mid1
        if arr[mid2] == key: return mid2
        if key < arr[mid1]: return ternary_search(l, mid1 - 1, key, arr)
        elif key > arr[mid2]: return ternary_search(mid2 + 1, r, key, arr)
        else: return ternary_search(mid1 + 1, mid2 - 1, key, arr)
    return -1

if __name__ == "__main__":
    print(ternary_search(0, 2, 2, [1,2,3]))''',
    
    '197_selection_sort.py': '''def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    print(selection_sort([3,1,2]))''',
    
    '198_insertion_sort_recursive.py': '''def insertion_sort_recursive(arr, n):
    if n <= 1: return
    insertion_sort_recursive(arr, n-1)
    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last

if __name__ == "__main__":
    arr = [3,1,2]
    insertion_sort_recursive(arr, len(arr))
    print(arr)''',
    
    '199_bubble_sort_recursive.py': '''def bubble_sort_recursive(arr, n):
    if n == 1: return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubble_sort_recursive(arr, n-1)

if __name__ == "__main__":
    arr = [3,1,2]
    bubble_sort_recursive(arr, len(arr))
    print(arr)''',
    
    '200_comb_sort.py': '''def get_next_gap(gap):
    gap = (gap * 10) // 13
    if gap < 1: return 1
    return gap

def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped == 1:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr

if __name__ == "__main__":
    print(comb_sort([3,1,2]))''',
    
    '201_pigeonhole_sort.py': '''def pigeonhole_sort(arr):
    my_min = min(arr)
    my_max = max(arr)
    size = my_max - my_min + 1
    holes = [0] * size
    for x in arr:
        holes[x - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + my_min
            i += 1
    return arr

if __name__ == "__main__":
    print(pigeonhole_sort([3,1,2]))''',
    
    '202_cycle_sort.py': '''def cycle_sort(arr):
    writes = 0
    for cycleStart in range(0, len(arr) - 1):
        item = arr[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, len(arr)):
            if arr[i] < item: pos += 1
        if pos == cycleStart: continue
        while item == arr[pos]: pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(arr)):
                if arr[i] < item: pos += 1
            while item == arr[pos]: pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1
    return arr

if __name__ == "__main__":
    print(cycle_sort([3,1,2]))''',
    
    '203_cocktail_sort.py': '''def cocktail_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped: break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        start = start+1
    return a

if __name__ == "__main__":
    print(cocktail_sort([3,1,2]))''',
    
    '204_gnome_sort.py': '''def gnome_sort(arr, n):
    index = 0
    while index < n:
        if index == 0: index = index + 1
        if arr[index] >= arr[index - 1]: index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
    return arr

if __name__ == "__main__":
    print(gnome_sort([3,1,2], 3))''',
    
    '205_bitonic_sort.py': '''def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)

if __name__ == "__main__":
    arr = [3, 7, 4, 8, 6, 2, 1, 5]
    bitonicSort(arr, 0, len(arr), 1)
    print(arr)''',
    
    '206_pancake_sort.py': '''def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def findMax(arr, n):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]: mi = i
    return mi

def pancake_sort(arr):
    curr_size = len(arr)
    while curr_size > 1:
        mi = findMax(arr, curr_size)
        if mi != curr_size-1:
            flip(arr, mi)
            flip(arr, curr_size-1)
        curr_size -= 1
    return arr

if __name__ == "__main__":
    print(pancake_sort([3,1,2]))''',
    
    '207_bogo_sort.py': '''import random

def is_sorted(data):
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def bogo_sort(data):
    while not is_sorted(data):
        random.shuffle(data)
    return data

if __name__ == "__main__":
    print(bogo_sort([3,1,2]))''',
    
    '208_stooge_sort.py': '''def stooge_sort(arr, l, h):
    if l >= h: return
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge_sort(arr, l, h - t)
        stooge_sort(arr, l + t, h)
        stooge_sort(arr, l, h - t)
    return arr

if __name__ == "__main__":
    arr = [3,1,2]
    print(stooge_sort(arr, 0, 2))''',
    
    '209_odd_even_sort.py': '''def odd_even_sort(arr, n):
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
    return arr

if __name__ == "__main__":
    print(odd_even_sort([3,1,2], 3))''',
    
    '210_strand_sort.py': '''def strand_sort(arr):
    if len(arr) <= 1: return arr
    result = []
    while len(arr) > 0:
        sublist = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if arr[i] >= sublist[-1]:
                sublist.append(arr.pop(i))
            else:
                i += 1
        merged = []
        while len(result) > 0 and len(sublist) > 0:
            if result[0] < sublist[0]: merged.append(result.pop(0))
            else: merged.append(sublist.pop(0))
        merged.extend(result)
        merged.extend(sublist)
        result = merged
    return result

if __name__ == "__main__":
    print(strand_sort([3,1,2]))'''
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

print("All 20 files pushed successfully!")
