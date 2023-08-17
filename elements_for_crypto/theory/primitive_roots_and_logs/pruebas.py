import sympy.ntheory as nt
from sympy.core import igcd

def units(m):
    return [k for k in range(1, m) if igcd(k,m) == 1]

def inverse_of(e, m):
    d = pow(e, nt.totient(m)-1, m)
    return d
    
def inverses_of(m):
    my_units = units(m)
    return [(a, inverse_of(a, m)) for a in my_units]

### verifing if ord_n(a) is divisor of n
def order_of_is_divisor(n):
    my_units = units(n)
    my_divisors = nt.divisors(n)
    for a in my_units:
        order = nt.n_order(a, n)
        print(f"order of {a} mod {n} is {order} and  respecto to {order} is divisor of {n}, that is {order in my_divisors}")

def primitive_root_generates_all(p):
    g = nt.primitive_root(p)
    all_powers = [g**k for k in range(1, p)]
    all_powers_residues = sorted([power % p for power in all_powers])
    return all_powers, all_powers_residues

# exploring powers
def set_of_all_powers(a, m):
    if igcd(a, m) == 1:
        list_powers = [pow(a, k, m) for k in range(nt.n_order(a, m))]
    else:
        list_powers = [pow(a, k, m) for k in range(nt.totient(m))]
    return set(list_powers)


if __name__ == "__main__":
    # print(primitive_root_generates_all(17))
    # print(primitive_root_generates_all(71))
    # print(inverses_of(12))
    print(set_of_all_powers(5, 14))