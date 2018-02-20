from sympy import nextprime
import numpy as np


# create private key pair
def generatekey(p, phi, secret, private):
    private2 = list(map(lambda x: (secret + phi[0]*x + phi[1]*x**2
                        + phi[2]*x**3 + phi[3]*x**4) % p, private))
    return private2


# Fermat's little theorem
def inv(x, p):
    if x < 0:
        x = x % p
    b = x
    for i in range(p - 3):
        b = b * x % p
    return b


# calculate the secret through Lagrange interpolation in finite filed
def lagrange(private, private2, p):
    tempi = 0
    for i in range(5):
        tempj = private2[i]
        for j in range(5):
            if j != i:
                tempj = (tempj * inv(private[i] - private[j], p)
                         * (-private[j])) % p
        tempi = (tempi + tempj) % p
    return tempi


p = nextprime(10000)
np.random.seed(579)
phi = np.random.randint(low=1, high=p-1, size=4)
private = np.random.randint(low=1, high=100, size=10)

secret = 30  # set secret
private2 = generatekey(p, phi, secret, private)


# randomly choose five persons to re-construct the secret
index = np.random.choice(10, 5, replace=False)
newprivate = [private[i] for i in index]
newprivate2 = [private2[i] for i in index]
recoversecret = lagrange(newprivate, newprivate2, p)
newprivate
print recoversecret
