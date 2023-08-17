import numpy as np
import sympy.ntheory as nt
import sympy as sy
# from tools_blocks2message import *
# from tools_message2blocks import *

def two_big_primes_res3mod4(n_min_digits):
    """INPUTS: n_min_digits (int), minimum number of digits for smallest prime
      OUTPUTS: tuple p (int), q (int). Big primes"""
    multiples = np.array([2,4,8])
    rand_m = np.random.choice(multiples)
    potentials_p = list(sy.sieve.primerange(n_min_digits, rand_m * n_min_digits))
    ps_res3mod4 = [p for p in potentials_p if p % 4 == 3]
    potentials_q = list(sy.sieve.primerange(2 * rand_m * n_min_digits, 3 * rand_m * n_min_digits))
    qs_res3mod4 = [q for q in potentials_q if q % 4 == 3]
    p, q = np.random.choice(np.array(ps_res3mod4)), np.random.choice(np.array(qs_res3mod4))
    return int(p), int(q)


if __name__ == "__main__":
    p, q = two_big_primes_res3mod4(100)
    print("primos: ", p, q)
    print("residuos al dividir por 4: ", p % 4, q % 4)
    numbers = list(range(11, 38))
    for num in numbers:
        if sy.ntheory.jacobi_symbol(num, 7919) == -1:
            print(f"{num} tiene simbolo de jacobi: ", sy.ntheory.jacobi_symbol(num, 7919))
    
    pass