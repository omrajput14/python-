def strand_sort(arr):
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
    print(strand_sort([3,1,2]))