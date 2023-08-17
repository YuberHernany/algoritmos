from crypto_ElGamal_new import *
import sympy.ntheory as nt
import numpy as np

def a_hat(e_hat, p, g):
    """INPUTS: e_hat (int), g (int) primite root of p. p (int) prime
    OUTPUTS: a_hat_ (int)"""
    a_hat_ = pow(g, e_hat, p)    
    return a_hat_

def signature(b, e_hat, gam, k, p, g):
    """INPUTS: b (int) ciphered block. e_hat (int) private key.
                gam (int) it is pow(g, k, p).
                k (int) coprime with p-1
                p (int) prime
                g (int) primitive root of p
        OUTPUTS: (s, a_hat_) (tuple) signature"""
    k_inv = pow(k, nt.totient(p)-1, p)
    s = ((b - e_hat * gam) * k_inv) % p
    a_hat_ = a_hat(e_hat, p, g)
    return s, a_hat_

def possible_values_for_k(number_of_blocks, p):
    """INPUTS: number_of_blocks (int) and determine the number of options for k
                p (int) prime.
        OUTPUTS: list of ints with len number_of_blocks (all the ints are coprimes with p-2)"""
    coprimes_with_p_minus_2 = [k for k in range(1, p-1) if igcd(k,p) == 1]
    coprimes_permuted = np.random.permutation(coprimes_with_p_minus_2)
    coprimes_casted_like_ints = [int(num) for num in coprimes_permuted]
    return coprimes_casted_like_ints[:number_of_blocks]

# def encrypt_ElGamal_with_signatures(blocks, p, g, a, e_hat):
#     N = len(blocks)
#     values_of_k = possible_values_for_k(N, p)
#     gams = [pow(g, k, p) for k in values_of_k]
#     signatures = [signature(b, e_hat, gam, k, p, g) for b, gam, k in zip(blocks, gams, values_of_k)]
#     encrypted = [encrypt_ElGamal_with_k_prefixed(list(b), p, g, a, k) for b, k in zip(blocks, values_of_k)]
#     encrypted_tuples = [(gam, beta) for gam, beta in zip(gams, encrypted)]
#     return signatures, encrypted_tuples
########################### It doesn't work

if __name__ == "__main__":
    # print(signature(11, 4, 8, 3, 29, 2))
    # print(possible_values_for_k(10, 29))
    message = 'cada'
    p, g, a = 79, 3, 9
    e = 2
    blocks = message2blocks(message, possible_len=2)
    print(blocks)
    # print(encrypt_ElGamal_with_signatures(blocks, p, g, a, e))
    pass