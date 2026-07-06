def build_suffix_array(txt):
    n = len(txt)
    suffixes = [(txt[i:], i) for i in range(n)]
    suffixes.sort(key=lambda x: x[0])
    return [suffix[1] for suffix in suffixes]

def kasai(txt, suffix_arr):
    n = len(suffix_arr)
    lcp = [0] * n
    inv_suff = [0] * n
    
    for i in range(n):
        inv_suff[suffix_arr[i]] = i
        
    k = 0
    for i in range(n):
        if inv_suff[i] == n - 1:
            k = 0
            continue
            
        j = suffix_arr[inv_suff[i] + 1]
        
        while i + k < n and j + k < n and txt[i + k] == txt[j + k]:
            k += 1
            
        lcp[inv_suff[i]] = k
        if k > 0:
            k -= 1
            
    return lcp

if __name__ == '__main__':
    txt = "banana"
    suff_arr = build_suffix_array(txt)
    
    print(f"Text: {txt}")
    print(f"Suffix Array: {suff_arr}")
    
    lcp = kasai(txt, suff_arr)
    print("LCP Array is:", lcp)
