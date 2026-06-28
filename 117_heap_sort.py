# Heap Sort Example
import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print("Original array:", nums)
    sorted_nums = heapsort(nums)
    print("Sorted array:", sorted_nums)
