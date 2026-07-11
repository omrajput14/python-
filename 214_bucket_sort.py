def bucketSort(arr):
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
