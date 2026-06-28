# Find Prime Factors Example
import math

def prime_factors(n):
    factors = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
        
    # n must be odd at this point
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
            
    if n > 2:
        factors.append(int(n))
    return factors

if __name__ == "__main__":
    num = 315
    print(f"Prime factors of {num}:", prime_factors(num))
