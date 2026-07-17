# 257. Perfect Number
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.

import math

def check_perfect_number(num):
    if num <= 1:
        return False
    
    divisors_sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors_sum += i
            if i * i != num:
                divisors_sum += num // i
                
    return divisors_sum == num

if __name__ == "__main__":
    print(check_perfect_number(28))  # True
    print(check_perfect_number(7))   # False
