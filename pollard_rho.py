"""
This is a simple, yet straight forward implementation of Pollard's rho algorithm for discrete logarithms
It computes X such that G^X = H mod P.

p does not need to be a safe prime.
"""
from gmpy2 import invert, gcd


def xab(x, a, b, params):
    """
    Pollard Step
    :param x:
    :param a:
    :param b:
    :return:
    """
    G, H, P, Q = params
    sub = x % 3 # Subsets

    if sub == 0:
        x = x*G % P
        a = (a+1) % Q
    elif sub == 1:
        x = x*H % P
        b = (b+1) % Q
    else:
        # sub == 2:
        x = x*x % P
        a = a*2 % Q
        b = b*2 % Q

    return x, a, b


def pollard(G, H, P):

    # P: prime
    # H:
    # G: generator
    Q = (P - 1)  # multiplicative sub group order

    x, a, b = 1, 0, 0
    X, A, B = x, a, b

    # for i in range(1, P):
    while True:
        # Hedgehog
        x, a, b = xab(x, a, b, (G, H, P, Q))

        # Hare
        X, A, B = xab(X, A, B, (G, H, P, Q))
        X, A, B = xab(X, A, B, (G, H, P, Q))

        if x == X:
            break

    num = a-A
    denum = B-b

    # It is necessary to compute the inverse to properly compute the fraction mod q
    # find gcd before solving linear equation denum*res = num mod Q
    gcdz = gcd(num, denum, Q)
    # print(f'gcds = {gcdz}')
    if gcdz == 1:  # standard solution
        res = invert(denum, Q)*num % Q  # divm(num, denum, Q)  # (inverse(denom, Q) * nom) % Q
    else:
        # needs a little bit more work
        # divide by gcd
        modz = Q//gcdz
        num = num//gcdz
        denum = denum//gcdz

        # baseline solution
        res0 = invert(denum, modz)*num % modz
        # check in solutions of the shape (denum/gcd)*res = (num/gcd) mod (Q/gcd) + k * (Q/gcd) (k in [0, gcd[) 
        for k in range(gcdz):
            res = res0+k*modz
            if verify(G, H, P, res):
                break
    return res


def verify(g, h, p, x):
    """
    Verifies a given set of g, h, p and x
    :param g: Generator
    :param h:
    :param p: Prime
    :param x: Computed X
    :return:
    """
    return pow(g, x, p) == h


if __name__ == '__main__':
    M = 424242

    args = [
        (2, 11, 59),
        (2, M, 5041259),
        (5, M, 87993167),
        (2, M, 1726565507),
        (7, M, 24455596799),
        (5, M, 368585361623),
        (11, M, 4520967464159),
        (5, M, 66008980226543),
        (5, M, 676602320278583),
        (2, M, 2075952270932339),
        (7, M, 21441211962585599)
    ]

    for arg in args:
        res = pollard(*arg)
        print(arg, ': ', res)
        print("Validates: ", verify(*arg, res))
        print()
