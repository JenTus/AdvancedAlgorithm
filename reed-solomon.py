import numpy.polynomial.polynomial as P


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
def mul(a, b, p):
    temp = P.polymul(a, b)
    e = [int(x % p) for x in temp]
    e = remove_zeros(e)
    return e


# addition of polynomails
def add(a, b, p):
    temp = P.polyadd(a, b)
    e = [int(x % p) for x in temp]
    e = remove_zeros(e)
    return e


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
    if len(a) < len(b):
        return [[0], a]
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
        i = i+1
    return [i-1, r, s, t, q]


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
    c = list(map(lambda i: (-i, 1), xi))  # construct the polynomial
    g_0 = reduce(lambda x, y: P.polymul(x, y), c)
    return list(map(lambda x: int(x % field), g_0))


# return the coefficients of g_1
# g(xi[i]) = eta[i]
def interpolation_polynomial(xi, eta, e, field):
    coeflist = 0
    for i in range(e):
        xi_j_list = [xi[j] for j in range(e) if j != i]
        xi_i = xi[i]
        xi_minus_xi_j = construct_polynomial(xi_j_list, field)
        lambnda_i = eta[i] * inv(evaluation(xi_minus_xi_j, xi_i, field), field)
        a = P.polymul(lambnda_i, xi_minus_xi_j)
        coeflist = P.polyadd(coeflist, a) % field
    return [int(i) for i in coeflist]


# deg g_h >= D, deg g_h+1 <D
def decode(xi, eta, e, d, field):
    g_0 = construct_polynomial(xi, field)
    g_1 = interpolation_polynomial(xi, eta, e, field)
    D = int((e + d + 1)/2)
    [l, r, s, t, q] = tee_pol(g_0, g_1, field)
    for i in range(len(r)):
        if (len(r[i]) - 1 >= D) & (len(r[i+1]) - 1 < D):
            divresult = div(r[i + 1], t[i + 1], field)
            break
    return divresult


#testing encoding
phi = [7, 6, 5, 4, 3]
psi = [0, 1, 2, 3, 4, 5, 6]
encoding(phi, psi, 11)


# testing
f = decode([1, 2, 3, 4, 5, 6], [3, 8, 6, 0, 7, 1], 6, 2, 13)[0]
print f
print encoding(f, [1, 2, 3, 4, 5, 6], 13)


# brute-force
pp = [3, 8, 6, 0, 7, 1]
for i in range(13):
    for j in range(13):
        tt = encoding([i, j], [1, 2, 3, 4, 5, 6], 13)
        temp = 0
        for z in range(len(tt)):
            if tt[z] != pp[z]:
                temp += 1
        if temp <= 2:
            print [i, j], tt
