import math
from functools import cmp_to_key

class Query:
    def __init__(self, L, R, id):
        self.L = L
        self.R = R
        self.id = id

block = 0

def compare(q1, q2):
    if q1.L // block != q2.L // block:
        return -1 if (q1.L // block < q2.L // block) else 1
    return -1 if (q1.R < q2.R) else 1

def query_results(a, m, queries):
    global block
    block = int(math.sqrt(len(a)))
    
    queries.sort(key=cmp_to_key(compare))
    currL, currR = 0, 0
    currSum = 0
    
    res = [0] * m
    for i in range(m):
        L = queries[i].L
        R = queries[i].R
        
        while currL < L:
            currSum -= a[currL]
            currL += 1
            
        while currL > L:
            currSum += a[currL - 1]
            currL -= 1
            
        while currR <= R:
            currSum += a[currR]
            currR += 1
            
        while currR > R + 1:
            currSum -= a[currR - 1]
            currR -= 1
            
        res[queries[i].id] = currSum
        
    return res

if __name__ == '__main__':
    a = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    queries = [Query(0, 4, 0), Query(1, 3, 1), Query(2, 4, 2)]
    m = len(queries)
    results = query_results(a, m, queries)
    print("Array:", a)
    for i in range(m):
        print(f"Sum of range [{queries[i].L}, {queries[i].R}] is {results[i]}")
