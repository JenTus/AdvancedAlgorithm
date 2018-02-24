"""tranditional_extended_eudlidean.py: All Calculations mod p"""


import numpy as np
from fractions import gcd


#  remove zeros as higher coefficients
def remove_zeros(x):
    for index in range(len(x)-1, -1, -1):
        if x[index] != 0:
            x = x[:][0:index + 1]
            return x
    return [0]


#  multiplication of polynomials
#  a = a_0 + a_1 * x + a_2 * x^2 ...
#  %p
def mul(a_0, b_0, p):
    if len(a_0) > len(b_0):
        a = b_0
        b = a_0
    else:
        a = a_0
        b = b_0
    c = [1 for i in range(len(a))]
    d = [[0 for i in range(len(a) + len(b) - 1)] for j in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b)):
            d[i][j + i] = a[i]*b[j]

    e = [x % p for x in np.dot(c, d)]
    e = remove_zeros(e)
    return e


# addition of polynomails
def add(a, b, p):
    if len(a) > len(b):
        b = b + [0 for i in range(len(a) - len(b))]
    else:
        a = a + [0 for i in range(len(b) - len(a))]
    c = [sum(x) % p for x in zip(a, b)]
    return remove_zeros(c)


# subtraction of polynomails
def sub(a, b, p):
    minorb = [-i for i in b]
    return add(a, minorb, p)


# Fermat's little theorem
def inv(x, p):
    if x < 0:
        x = x % p
    b = x
    for i in range(p - 3):
        b = b * x % p
    return b


#  polydiv
#  return q and r
def div(a, b, p):
    r = a[:]
    mu = inv(b[-1], p)
    etalist = []

    for i in range(len(a) - len(b), -1, -1):
        if len(r) == len(b) + i:
            eta = [0 if x != i else r[-1] * mu for x in range(i+1)]
            r = sub(r, mul(eta, b, p), p)
        else:
            eta = [0]
        etalist.append(eta)

    q = reduce(lambda x, y: add(x, y, p), etalist)
    return [q, r]


#  traditional extended eudlidean algorithm
#  for values
def tee(f, g):
    r = [f, g]
    s = [1, 0]
    t = [0, 1]
    q = [0, 0]
    i = 1
    while r[i] != 0:
        r = r + [0]
        s = s + [0]
        q = q + [0]
        t = t + [0]
        q[i] = r[i-1] // r[i]
        r[i+1] = r[i-1] - q[i]*r[i]
        s[i+1] = s[i-1] - q[i]*s[i]
        t[i+1] = t[i-1] - q[i]*t[i]
        i = i+1
    return [i-1, r, s, t]


#  traditional extended eudlidean algorithm
#  for polynomials
def tee_pol(f, g, p):
    r = [f, g]
    s = [[1], [0]]
    t = [[0], [1]]
    q = [[0]]
    i = 1
    while sum(r[i]) != 0:
        q.append(div(r[i-1], r[i], p)[0])
        r_temp = sub(r[i-1], mul(q[i], r[i], p), p)
        s_temp = sub(s[i-1], mul(q[i], s[i], p), p)
        t_temp = sub(t[i-1], mul(q[i], t[i], p), p)
        r.append(r_temp)
        s.append(s_temp)
        t.append(t_temp)
        #  print "i= %d, r = %s, s = %s, t = %s" %(i,r[i],s[i], t[i])
        i = i+1
    return [i-1, r, s, t, q]


#  testing
[l, r, s, t] = tee(1234567, 123)
print("r[l] is: %s, t[l] is: %s" % (r[l], t[l]))

[l, r, s, t, q] = tee_pol([1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1], 2)
print(r[l])

[l, r, s, t, q] = tee_pol([0, 9, 0, 2, 4, 9, 3, 5, 1], [5, 7, 5, 2, 10, 9, 6, 7], 11)
gcd(1234567, 123)
