"""
This is a simple, yet straight forward implementation of Pollard's rho algorithm for discrete logarithms
It computes X such that G^X = H mod P.

Too keep this implementation simple p must be a safe prime, such that
there is a prime q for which p = 2q+1 holds true.

The algorithm was designed using a "Hase/Igel" (German: Rabbit/Hedgehog) approach.
Meaning there are two independent computations of Pollard's rho at different speeds.
The algorithm stops, when the slower "Igel" has overtaken the faster rabbit and their X values are equal.
We call this a collision.

This program was developed as part of an assignment in the lecture
"Security and Cryptology" by Prof. Weber at Saarland University of Applied Sciences (htw saar)
"""


def ext_euclid(a, b):
    """
    Extended Euclidean Algorithm
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a, 1, 0
    else:
        d, xx, yy = ext_euclid(b, a % b)
        x = yy
        y = xx - (a / b) * yy
        return d, x, y


def inverse(a, n):
    """
    Inverse of a in mod n
    :param a:
    :param n:
    :return:
    """
    return ext_euclid(a, n)[1]


def xab(x, a, b, (G, H, P, Q)):
    """
    Pollard Step
    :param x:
    :param a:
    :param b:
    :return:
    """
    sub = x % 3 # Subsets

    if sub == 0:
        x = x*G % P
        a = (a+1) % Q

    if sub == 1:
        x = x * H % P
        b = (b + 1) % Q

    if sub == 2:
        x = x*x % P
        a = a*2 % Q
        b = b*2 % Q

    return x, a, b


def pollard(G, H, P):

    # P: prime
    # H:
    # G: generator
    Q = (P - 1) / 2  # sub group


    x = G*H
    a = 1
    b = 1

    X = x
    A = a
    B = b

    # Do not use range() here. It makes the algorithm amazingly slow.
    for i in xrange(1, P):
        # Who needs pass-by reference when you have Python!!! ;)

        # Hedgehog
        x, a, b = xab(x, a, b, (G, H, P, Q))

        # Rabbit
        X, A, B = xab(X, A, B, (G, H, P, Q))
        X, A, B = xab(X, A, B, (G, H, P, Q))

        if x == X:
            break


    nom = a-A
    denom = B-b

    print nom, denom

    # It is necessary to compute the inverse to properly compute the fraction mod q
    res = (inverse(denom, Q) * nom) % Q

    # I know this is not good, but it does the job...
    if verify(G, H, P, res):
        return res

    return res + Q


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
    print arg, ': ', res
    print "Validates: ", verify(arg[0], arg[1], arg[2], res)
    print


