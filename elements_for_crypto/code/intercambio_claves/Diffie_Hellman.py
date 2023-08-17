import sympy.ntheory as nt
import random

p = nt.prime(1000)
g = nt.primitive_root(p)

m_Dan = random.randint(1, 1000)
n_Hellen = random.randint(1, 1000)

sent_by_Hellen = pow(g, n_Hellen, p)
sent_by_Dan = pow(g, m_Dan, p)

key = pow(sent_by_Dan, n_Hellen, p)
print(key)