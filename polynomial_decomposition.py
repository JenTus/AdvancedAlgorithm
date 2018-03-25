from traditional_extended_eudlidean import polynomial


# calculate the derivative of a polynomial poly
# %p
def derivative_polynomial(poly, p):
    result = []
    for i in range(len(poly)):
        if i == 0:
            continue
        else:
            result.append(poly[i] * i % p)
    return result


# p_th root of the polynomial
def root(poly, p):
    result = []
    for i in range(len(poly)):
        if i % p == 0:
            result.append(poly[i])
    return result


f = [2, 2, 1, 0, 2, 2, 2, 0, 2, 2, 1, 1, 1, 1]
f_deri = derivative_polynomial(f, 3)
P = polynomial()
u = P.gcd(f, f_deri, 3)  # gcd
[v, _] = P.div(f, u, 3)
[w, _] = P.div(f, P.gcd(f, P.exp(v, (len(f)-1), 3), 3), 3)
root_w = root(w, 3)
g = P.mul(root_w, v, 3)  # square-free part of f

N = 2028455971
s = 702505371
t = 188270011

(s - t)*(s + t) / N
