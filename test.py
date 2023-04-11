from pollard_rho  import pollard
import time

P = 401  # not a safe prime
G = 7
H = 385

print(f'x such that {G}**x = {H} mod {P}')

tic = time.time()
x = pollard(G, H, P)
print(f'elapsed time = {time.time()-tic}')
print(f'x = {x}')  # expected : 192
