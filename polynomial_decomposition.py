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


f = [2, 2, 1, 0, 2, 2, 2, 0, 2, 2, 1, 1, 1, 1]
f_deri = derivative_polynomial(f, 3)
P = polynomial()
u = P.gcd(f, f_deri, 3)  # gcd
[v, _] = P.div(f, u, 3)
w = P.div(P.gcd(f, P.exp(v, len(f) - 1, 3)))

P.exp(v, 1, 3)
print v
