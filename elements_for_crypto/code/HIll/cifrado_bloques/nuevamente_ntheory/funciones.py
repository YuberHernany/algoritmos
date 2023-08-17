import sympy.ntheory as nt
import sympy as sy

# how create a prime
third_prime = nt.prime(3)
# print(third_prime)

# how calculate gcd
d = sy.igcd(12, 8)
# print(d)

# verify if are coprimes 

def are_coprimes(m, n):
    return sy.igcd(m, n) == 1

# list of coprimes with
def coprimes_with(n):
    coprimes = [m*are_coprimes(m,n) for m in range(1, n) if are_coprimes(m,n)]
    return coprimes

# print(coprimes_with(5))
# print(coprimes_with(8))

def potental_exponents_for_rsa(p, q):
    """p, q (integers). primes p and q"""
    return coprimes_with((p-1) * (q-1))

# print(potental_exponents_for_rsa(11,13))

# powers Ej: pow(base, exponent, modulo)
a = pow(2,4,10)
# print(a)

# dicrete logarithms
# nt.discrete_log(n, a, b) # logarithm of a to the base b mod n
p = 7
l = nt.discrete_log(p, 6, 5) # solves 5 ** l =  6 (mod p) # l is 3
# print(pow(5, l, p)) # verifing that l is solution # prints 6

# square roots
# nt.sqrt_mod(a, p) # solves x ** 2 = a (mod p)
x = nt.sqrt_mod(2, 7) # solves x ** 2 = 6 (mod 7) # x is 3
# print(x)

