# 306. Additive Number
# An additive number is a string whose digits can form an additive sequence.

def is_additive_number(num):
    n = len(num)
    for i in range(1, n):
        for j in range(i+1, n):
            s1, s2 = num[:i], num[i:j]
            if (s1.startswith('0') and len(s1) > 1) or (s2.startswith('0') and len(s2) > 1): continue
            
            n1, n2 = int(s1), int(s2)
            k = j
            while k < n:
                n3 = n1 + n2
                s3 = str(n3)
                if not num.startswith(s3, k): break
                k += len(s3)
                n1, n2 = n2, n3
            if k == n: return True
    return False

if __name__ == "__main__":
    print(is_additive_number("112358"))
