"""tranditional_extended_eudlidean.py: All Calculations mod p"""


import numpy as np
# from fractions import gcd


class polynomial:

    #  remove zeros as higher coefficients
    def remove_zeros(self, x):
        for index in range(len(x)-1, -1, -1):
            if x[index] != 0:
                x = x[:][0:index + 1]
                return x
        return [0]

    #  multiplication of polynomials
    #  a = a_0 + a_1 * x + a_2 * x^2 ...
    #  %p
    def mul(self, a_0, b_0, p):
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
        e = self.remove_zeros(e)
        return e

    # addition of polynomails
    def add(self, a, b, p):
        if len(a) > len(b):
            b = b + [0 for i in range(len(a) - len(b))]
        else:
            a = a + [0 for i in range(len(b) - len(a))]
        c = [sum(x) % p for x in zip(a, b)]
        return self.remove_zeros(c)

    # subtraction of polynomails
    def sub(self, a, b, p):
        minorb = [-i for i in b]
        return self.add(a, minorb, p)

    # Fermat's little theorem
    def inv(self, x, p):
        if x < 0:
            x = x % p
        b = x
        for i in range(p - 3):
            b = b * x % p
        return b

    #  polydiv classical algorithm for polynomial division
    #  return q and r
    def div(self, a, b, p):
        if len(a) < len(b):
            return [[0], a]
        r = a[:]
        mu = self.inv(b[-1], p)
        etalist = []

        for i in range(len(a) - len(b), -1, -1):
            if len(r) == len(b) + i:
                eta = [0 if x != i else r[-1] * mu for x in range(i+1)]
                r = self.sub(r, self.mul(eta, b, p), p)
            else:
                eta = [0]
            etalist.append(eta)

        q = reduce(lambda x, y: self.add(x, y, p), etalist)
        return [q, r]

    #  traditional extended eudlidean algorithm
    #  for polynomials
    def tee_pol(self, f, g, p):
        r = [f, g]
        s = [[1], [0]]
        t = [[0], [1]]
        q = [[0]]
        i = 1
        while sum(r[i]) != 0:
            q.append(self.div(r[i-1], r[i], p)[0])
            r_temp = self.sub(r[i-1], self.mul(q[i], r[i], p), p)
            s_temp = self.sub(s[i-1], self.mul(q[i], s[i], p), p)
            t_temp = self.sub(t[i-1], self.mul(q[i], t[i], p), p)
            r.append(r_temp)
            s.append(s_temp)
            t.append(t_temp)
            #  print "i= %d, r = %s, s = %s, t = %s" %(i,r[i],s[i], t[i])
            i = i+1
        return [i-1, r, s, t, q]


# p = polynomial()
# f = [4, 5, 3, 2, 9, 8, 1, 3, 9, 5, 7]
# g = [5, 7, 5, 5, 1, 7, 4, 5, 8]
# print p.div(f, g, 11)
# test the classical division algorithm
# f_tilde = [0, 0, 0, 0, 0, 0, 1, 3, 9, 5, 7]
# g_tilde = [0, 0, 0, 0, 0, 0, 4, 5, 8]

# div(f, g, 11)
# div(f_tilde, g_tilde, 11)
# f[-2:]
#  testing
# [l, r, s, t] = tee(1234567, 123)
# print("r[l] is: %s, t[l] is: %s" % (r[l], t[l]))

# [l, r, s, t, q] = tee_pol([1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1], 2)
# print(r[l])

# [l, r, s, t, q] = tee_pol([0, 9, 0, 2, 4, 9, 3, 5, 1],
#                           [5, 7, 5, 2, 10, 9, 6, 7], 11)
# gcd(1234567, 123)
