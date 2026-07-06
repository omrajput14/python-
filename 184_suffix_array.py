def build_suffix_array(txt):
    n = len(txt)
    suffixes = [(txt[i:], i) for i in range(n)]
    
    # Sort suffixes based on the substring
    suffixes.sort(key=lambda x: x[0])
    
    # Extract the original indices to form the suffix array
    suffix_arr = [suffix[1] for suffix in suffixes]
    
    return suffix_arr

def search(pat, txt, suff_arr):
    n = len(txt)
    m = len(pat)
    l = 0
    r = n - 1
    
    while l <= r:
        mid = l + (r - l) // 2
        res = txt[suff_arr[mid]:suff_arr[mid]+m]
        
        if res == pat:
            print("Pattern found at index", suff_arr[mid])
            return
        elif res < pat:
            l = mid + 1
        else:
            r = mid - 1
            
    print("Pattern not found")

if __name__ == '__main__':
    txt = "banana"
    pat = "nan"
    
    print(f"Text: {txt}")
    suff_arr = build_suffix_array(txt)
    print("Suffix Array for the text is:", suff_arr)
    
    print(f"Searching for pattern: {pat}")
    search(pat, txt, suff_arr)
