from sympy import nextprime
import numpy as np
import lagrange

# create public key
def generatepublickey(p, phi, secret, private):
    public = list(map(lambda x: (secret + phi[0]*x + phi[1]*x**2 + phi[2]*x**3
                      + phi[3]*x**4) % p, private))
    return public


p = nextprime(100000000)
np.random.seed(123)
phi = np.random.randint(low=1, high=p-1, size=4)
private = np.random.randint(low=1, high=100, size=10)


secret = 30  # set secret
public = generatepublickey(p, phi, secret, private)

private_pulic_key = [(private[i], public[i]) for i in range(10)]

lagrange([(1,15), (2,9), (3,3)], 17)

private_pulic_key
private_pulic_key[0:5]
