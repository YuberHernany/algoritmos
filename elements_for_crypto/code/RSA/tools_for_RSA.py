import numpy as np
import sympy.ntheory as nt
import sympy as sy
from tools_blocks2message import *
from tools_message2blocks import *

def two_big_primes(n_min_digits):
    """INPUTS: n_min_digits (int), minimum number of digits for smallest prime
      OUTPUTS: tuple p (int), q (int). Big primes"""
    multiples = np.array([2,4,8])
    rand_m = np.random.choice(multiples)
    potentials_p = list(sy.sieve.primerange((10**n_min_digits), rand_m * (10**n_min_digits)))
    potentials_q = list(sy.sieve.primerange(2 * rand_m * (10**n_min_digits), 3 * rand_m * (10**n_min_digits)))
    p, q = np.random.choice(np.array(potentials_p)), np.random.choice(np.array(potentials_q))
    return int(p), int(q)

def random_coprime_with(k):
    """INPUTS: k (int)
      OUTPUTS: e (int) coprime with k selected randomly"""
    I_have_a_coprime = False
    while not I_have_a_coprime:
        potential_coprime = np.random.randint(2, k)
        if sy.igcd(k, potential_coprime) == 1:
            I_have_a_coprime = True
    return int(potential_coprime)

def init_keys(n_min_digits):
    """INPUT: n_min_digits (int) quantity of digits in the shortest prime"""
    """OUTPUTS: tuple p, q, m, e"""
    p, q = two_big_primes(n_min_digits)
    m = int(p * q)
    e = random_coprime_with(nt.totient(m))
    return p, q, m, e

def encode_rsa(m, e, plane_blocks):
    encrypted_blocks = [pow(a, e, m) for a in plane_blocks]
    return encrypted_blocks

def decode_rsa(m, d, encrypted_blocks):
    decrypted_blocks = [pow(b, d, m) for b in encrypted_blocks]
    return decrypted_blocks

def inverse_of(e, module):
    d = pow(int(e), int(nt.totient(module)-1), int(module))
    return d

if __name__ == "__main__":
    # print(two_big_primes(3))
    # p, q, m, e = init_keys(3)
    # print(p, q, m, e)
    # print(f"Working with arithmetic module {m}")
    # phi_m = (p-1) * (q-1)
    # d = inverse_of(int(e), phi_m)
    # d = pow(int(e), int(nt.totient(phi_m)-1), int(phi_m))
    # message = 'el enfoque es la clave del exito si quieres que los algoritmos funcionen'
    # plane_blocks = message2blocks(message)
    # print("plane blocks: ")
    # print(plane_blocks)
    # encoded = encode_rsa(m, e, plane_blocks)
    # print("Encoded blocks: ")
    # print(encoded)
    # decoded = decode_rsa(m, d, encoded)
    # print("Original blocks corresponding to Original message: ")
    # print(decoded)
    # print(blocks2message(decoded))


    # another proof
    # message = 'algo'
    # print(message2blocks(message))
    # p, q = 11,17
    # m = p * q
    # phi_m = nt.totient(m)
    # e = 7
    # plane_blocks = [112, 21, 7, 26]
    # encoded = encode_rsa(m, e, plane_blocks)
    # d = inverse_of(e, phi_m)
    # print(encoded)
    # print(d)
    # decoded = decode_rsa(m, d, encoded)
    # print(decoded)
    # print(blocks2message(decoded))
    pass 