"""tranditional_extended_eudlidean.py: All Calculations are in mod 2"""


import numpy as np
from fractions import gcd


#  remove zeros as higher coefficients
def remove_zeros(x):
    for i in range(len(x)):
        index = len(x) - 1 - i
        if x[index] != 0:
            x = x[:][0:index + 1]
            break
    return x


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


#  polydiv
#  return q and r
def div(a, b, p):
    r = a[:]
    q = [0 for i in range(len(a))]

    while len(r) >= len(b):
        q[len(r) - len(b)] = 1
        b_q = [0 for i in range(len(r) - len(b))] + b[:]  # b multiply q
        r = add(r, [-x for x in b_q], p)

        for i in range(len(r)):
            index = len(r) - 1 - i
            if index == 0:
                return [q, r]
            if r[index] != 0:
                r = r[:][0:index+1]
                break

    q = remove_zeros(q)
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
def tee_pol(f, g):
    r = [f, g]
    s = [[1], [0]]
    t = [[0], [1]]
    q = [[0]]
    i = 1
    while sum(r[i]) != 0:
        q.append(div(r[i-1], r[i])[0])
        r_temp = add(r[i-1], [-x for x in mul(q[i], r[i])])
        s_temp = add(s[i-1], [-x for x in mul(q[i], s[i])])
        t_temp = add(t[i-1], [-x for x in mul(q[i], t[i])])
        r.append(r_temp)
        s.append(s_temp)
        t.append(t_temp)
        #  print "i= %d, r = %s, s = %s, t = %s" %(i,r[i],s[i], t[i])
        i = i+1
    return [i-1, r, s, t]


#  testing
[l, r, s, t] = tee(1234567, 123)
print("r[l] is: %s, t[l] is: %s" % (r[l], t[l]))

[l, r, s, t] = tee_pol([1, 1, 0, 1, 1], [1, 0, 0, 0, 1])
print(r[l])

gcd(1234567, 123)
