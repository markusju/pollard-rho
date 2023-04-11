
# Pollard's Rho Algorithm for discrete logarithms in Python

This is a simple, yet straight forward implementation of Pollard's rho algorithm for discrete logarithms.

It computes $x$ such that $g^x = h\ mod\ p$

$p$ does not need to be a safe prime.

The algorithm was designed using a [Hare and the Hedgehog](https://en.wikipedia.org/wiki/The_Hare_and_the_Hedgehog) approach.

Meaning there are two independent computations of Pollard's rho at different speeds.
The algorithm stops, when the slower hedgehog has overtaken the faster hare and their $X$ values are equal.

This software was initially built for educational purposes. This version makes use of gmpy2 package to compute the modular inverse and the gcd. The installation of [gmpy2](https://pypi.org/project/gmpy2) is required.

This program was developed as part of an assignment in the lecture
"Security and Cryptography" by Prof. Weber at Saarland University of Applied Sciences (htw saar)
