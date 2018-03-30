import math
from sympy.ntheory.primetest import isprime
# Given an integer N ∈ Z ≥2 as input, design an algorithm that either
# (i) outputs a prime p and a positive integer a such that N = p a or
# (ii) asserts that N is not a prime power.


# Given integers N, k ∈ Z ≥2 as input, find the largest integer b
# such that b ** k ≤ N .
# when we find the exact b ** k == N, flag = 1
# when we find the b **k < N, flag = 0
def find_largest_b(N, k):

    def next_b(b_pre, b_next):
        if b_next ** k < N:
            return next_b(b_next, 2 * b_next)
        elif b_next ** k == N:
            return [1, b_next]
        else:
            if (b_pre + b_next) / 2 == b_pre:
                return [0, b_pre]
            else:
                return next_b(b_pre, (b_pre + b_next) / 2)

    return next_b(1, 1)


# b^^i = N
def find_prime_power(N):
    for i in range(2, int(math.log(N, 2) + 1)):
        [flag, b] = find_largest_b(N, i)
        if flag == 1:
            if isprime(b):
                return [b, i]
    return str(N) + " is not a prime power"


print find_prime_power(4**10)
print find_prime_power(3**10)
