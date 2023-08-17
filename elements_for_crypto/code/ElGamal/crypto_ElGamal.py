import numpy as np
import sympy.ntheory as nt
import sympy as sy
from tools_blocks2message import *
from tools_message2blocks import *

def big_prime(n_min_digits_for_prime):
    """INPUTS: n_min_digits_for_prime (int)
      OUTPUTS: p (int) Big prime"""
    multiples = np.array([2,4,8])
    rand_m = np.random.choice(multiples)
    potentials_p = list(sy.sieve.primerange(n_min_digits_for_prime, rand_m * n_min_digits_for_prime))
    p= np.random.choice(np.array(potentials_p))
    return int(p)

def get_public_key(n_min_digits_for_prime):
    """INPUTS: n_min_digits_for_prime (int)
    OUTPUTS: tuple of ints p, g, a: prime, primitive root and
            residue of exponent"""
    p = big_prime(n_min_digits_for_prime)
    g = nt.primitive_root(p)
    e = int(np.random.randint(1, p)) # private
    a = pow(g, e, p)
    return p, g, a

def randint_between_1_and_p_minus_2(p):
    """INPUTS: p (int) prime
    OUTPUTS:   k (int) random such that 1 <= k <= p-2"""
    k = int(np.random.randint(1, p-1))
    return k

def gamma(g, k, p):
    """INPUTS: g (int) primitive root, k (int), p (int) prime
    OUTPUTS:  gam (int)"""
    gam = pow(g, k, p)
    return gam

def factor(a, k, p):
    """INPUTS: a (int), k (int), p (int) prime
    OUTPUTS:  residue (int)"""
    residue = pow(a, k, p)
    return residue

def encrypt_ElGamal(blocks, p, g, a):
    """INPUTS: blocks (list of ints). p (int) prime, 
        g (int) primitive root of p, a (int) residue of exponent
    OUTPUTS: list of ints encrypted with ElGamal"""
    k = randint_between_1_and_p_minus_2(p)
    a_to_k = factor(a, k, p)
    encrypted = [(a_to_k * num) % p for num in blocks]
    return encrypted

def encrypt_ElGamal_with_k_prefixed(blocks, p, g, a, k):
    """INPUTS: blocks (list of ints). p (int) prime, 
        g (int) primitive root of p, a (int) residue of exponent
        k (int) it is supose randint, but here is used for verifications
    OUTPUTS: list of ints encrypted with ElGamal"""
    a_to_k = factor(a, k, p)
    encrypted = [(a_to_k * num) % p for num in blocks]
    return encrypted

def decrypt_ElGamal(blocks_encrypted, p, g, a, e, k):
    """INPUTS: blocks_encrypted (list of ints). p (int) prime. 
        g (int) primitive roots of p. a (int) residue of exponent.
        e (int) private key. k (int) it is suposed randint used for previous encryption
    OUTPUTS: decrypted (list of ints)"""
    gam = gamma(g, k, p)
    factor_decrypt = pow(gam, p - 1 - e, p)
    decrypted = [(factor_decrypt * num) % p for num in blocks_encrypted]
    return decrypted
    
if __name__ == "__main__":

    pass