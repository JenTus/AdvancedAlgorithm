# square and multiply modular expoentiation
from traditional_extended_eudlidean import polynomial
P = polynomial()


# suppose p is the characteristic of the field F_p
def square_and_multiply(f, g, m, p):
    [_, temp] = P.div(f, g, p)
    result = [1]
    while m != 0:
        m, flag = m / 2, m % 2
        if flag == 1:
            [_, result] = P.div(P.mul(temp, result, p), g, p)
        [_, temp] = P.div(P.mul(temp, temp), g, p)
    return result
