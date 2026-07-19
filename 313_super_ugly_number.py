# 313. Super Ugly Number
# A super ugly number is a positive integer whose prime factors are in the array primes.

def nth_super_ugly_number(n, primes):
    ugly = [1] * n
    idx = [0] * len(primes)
    vals = [p for p in primes]
    
    for i in range(1, n):
        nxt = min(vals)
        ugly[i] = nxt
        for j in range(len(primes)):
            if vals[j] == nxt:
                idx[j] += 1
                vals[j] = ugly[idx[j]] * primes[j]
    return ugly[-1]

if __name__ == "__main__":
    print(nth_super_ugly_number(12, [2,7,13,19]))
