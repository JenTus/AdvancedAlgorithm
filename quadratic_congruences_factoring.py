from modular_multiplicative_inverse import inverse
from sympy import sieve

I = inverse()
I.inv(3, 4)


N = 2028455971
s = 702505371
t = 188270011

print I.gcd(s, N)
print I.gcd(t, N)
a = I.gcd(s + t, N)
b = I.gcd(s - t, N)
N / I.gcd(s - t, N)
44027*46073


sieve.search(a)
sieve.search(b)
