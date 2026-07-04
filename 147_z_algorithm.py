def getZarr(string, z):
    n = len(string)
    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1

def search_z_algorithm(text, pattern):
    concat = pattern + "$" + text
    l = len(concat)
    z = [0] * l
    getZarr(concat, z)
    
    results = []
    for i in range(l):
        if z[i] == len(pattern):
            results.append(i - len(pattern) - 1)
            
    return results

if __name__ == '__main__':
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    matches = search_z_algorithm(text, pattern)
    if matches:
        for m in matches:
            print(f"Pattern found at index {m}")
    else:
        print("Pattern not found")
