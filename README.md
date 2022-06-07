
# Pollard's Rho Algorithm for discrete logarithms in Python

This is a simple, yet straight forward implementation of Pollard's rho algorithm for discrete logarithms.

It computes $x$ such that $g^x = h\ mod\ p$

$p$ must be a safe prime, such that there is a prime $q$ for which $p = 2q+1$ holds true.

The algorithm was designed using a [Hare and the Hedgehog](https://en.wikipedia.org/wiki/The_Hare_and_the_Hedgehog) approach.

Meaning there are two independent computations of Pollard's rho at different speeds.
The algorithm stops, when the slower hedgehog has overtaken the faster hare and their $X$ values are equal.

This software was built for educational purposes and could be improved regarding efficiency:
* Computation of the Inverse could be solved using Fermat's Little Theorem instead of the Euclidean Algorithm

This program was developed as part of an assignment in the lecture
"Security and Cryptography" by Prof. Weber at Saarland University of Applied Sciences (htw saar)
