
# Pollard's Roh Algorithm for discrete logarithms in Python

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

The program is pretty self explanatory and contains a set of sample values. Feel free to adjust these or adapt the program to your needs.
