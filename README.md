
# Pollard's Rho Algorithm for discrete logarithms in Python

This is a simple, yet straight forward implementation of Pollard's rho algorithm for discrete logarithms
It computes X such that G^X = H mod P.

p must be a safe prime, such that there is a prime q for which p = 2q+1 holds true.

The algorithm was designed using a "Hase/Igel" (German: Rabbit/Hedgehog) approach.
Meaning there are two independent computations of Pollard's rho at different speeds.
The algorithm stops, when the slower "Igel" has overtaken the faster rabbit and their X values are equal.

This program was developed as part of an assignment in the lecture
"Security and Cryptography" by Prof. Weber at Saarland University of Applied Sciences (htw saar)