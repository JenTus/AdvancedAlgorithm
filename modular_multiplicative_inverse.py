# ax - 1 (mod m)
# contrain the greatest common divisor
from sympy.ntheory.primetest import isprime


class inverse:
    # traditional extended euclidean algorithm
    def tee(self, f, g):
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

    # inverse based on traditional extended euclidean algorithm
    def inv(self, a, m):
        [l, r, s, _] = self.tee(a, m)
        if r[l] == 1:
            return s[l] % m
        else:
            return "the inverse does not exist"

    def gcd(self, a, m):
        [l, r, s, _] = self.tee(a, m)
        return r[l]

    # inverse based on Fermat little theorem
    def inv_fermat(self, a, n):
        if isprime(n):
            if a < 0:
                a = a % n
            b = a
            for i in range(n - 3):
                b = b * a % n
            return b
        else:
            return "n is not prime"


# testing
# I = inverse()
# print I.inv_fermat(-3, 8)
# print I.inv(-3, 8)
