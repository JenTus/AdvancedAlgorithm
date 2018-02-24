import numpy.polynomial.polynomial as P
from sympy.abc import x
from sympy import *

# evaluation at single potint
# phi_0 + phi_1 * num + phi_2 * num^2 + ... % field
def evaluation(phi, num, field):
    v = 0
    for i in range(len(phi)):
        v = v + phi[i]*(num**i)
    v = v % field
    return v


# encoding at multiple points
# psi = [num1, num2, ...]
def encoding(phi, psi, field):
    return list(map(lambda x: evaluation(phi, x, field), psi))


# construct the polynomial, return the coefficiients of g_0
# g_0 = (x - xi_0)(x - xi_1)...(x - xi_e)
def construct_polynomial(xi, field):
    c = list(map(lambda x: (-x, 1), xi))  # construct the polynomial
    g_0 = reduce(lambda x, y: P.polymul(x, y), c)
    return list(map(lambda x: int(x % field), g_0))


# Fermat's little theorem
def inv(x, p):
    if x < 0:
        x = x % p
    b = x
    for i in range(p - 3):
        b = b * x % p
    return b


# return the coefficients of g_1
# g(xi[i]) = eta[i]
def interpolation_polynomial(xi, eta, e, field):
    l = 0
    for i in range(e):
        tempj = eta[i]
        xij = [j for j in range(e) if j != i]
        for j in range(e):
            if j != i:
                tempj = (tempj * inv(xi[i] - xi[j], field)) % field
        a = P.polymul(tempj, construct_polynomial(xij, field))
        l = P.polyadd(l, a) % field
    return [int(i) for i in l]


#traditional extended euclidean algorithm
#input g_0, g_1



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




g_0 = construct_polynomial([0, 1, 2, 3, 4, 5, 6, 7], 11)
g_1 = interpolation_polynomial([0, 1, 2, 3, 4, 5, 6, 7], [5, 7, 1, 2, 9, 4, 1, 5], 8, 11)
g0 = reduce((lambda i, j: i + j),
            map(lambda i: i[0] * x ** i[1], zip(g_0, range(len(g_0)))))

g1 = reduce((lambda i, j: i + j),
            map(lambda i: i[0] * x ** i[1], zip(g_1, range(len(g_1)))))


g0
g1

g0

sympy.pquo(x**8, 5*x**7, domain = ZZ)
from sympy import degree
temp = 0
for i in range(len(a)):
    temp = temp + a[i] * x**i
temp
