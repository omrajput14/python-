def find_majority_element(arr):
    candidate = -1
    votes = 0
    
    # Phase 1: Find a candidate
    for i in range(len(arr)):
        if votes == 0:
            candidate = arr[i]
            votes = 1
        elif arr[i] == candidate:
            votes += 1
        else:
            votes -= 1
            
    # Phase 2: Verify candidate
    count = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            count += 1
            
    if count > len(arr) // 2:
        return candidate
    else:
        return -1

if __name__ == '__main__':
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(f"Array: {arr}")
    res = find_majority_element(arr)
    if res != -1:
        print(f"Majority element is {res}")
    else:
        print("No majority element found")
