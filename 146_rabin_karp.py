def search_rabin_karp(pat, txt, q=101):
    M = len(pat)
    N = len(txt)
    d = 256
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    results = []
    
    if M > N:
        return results

    for i in range(M - 1):
        h = (h * d) % q
        
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q
        
    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1
            if j == M:
                results.append(i)
                
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t = t + q
                
    return results

if __name__ == '__main__':
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"
    print(f"Text: {txt}")
    print(f"Pattern: {pat}")
    matches = search_rabin_karp(pat, txt)
    if matches:
        for m in matches:
            print(f"Pattern found at index {m}")
    else:
        print("Pattern not found")
