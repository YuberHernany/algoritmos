import numpy as np
import pandas as pd
import sympy.ntheory as nt
from sympy import igcd

def tabla_potencias(m, k):
    """m: int, module. k:int, max potencia """
    arr = np.fromfunction(lambda i,j: (((i+1)**(j+1))%m)*((i+1)*(j+1)>=1), (m-1,k), dtype=int)
    tabla = pd.DataFrame(arr,
                         columns=[f'a^{k}' for k in range(1, k+1)],
                         index=[k for k in range(1, m)])
    return tabla

# print(tabla_potencias(5,5))
#
# for p in nt.primerange(2, 10):
#     print(tabla_potencias(p, p))
# print(tabla_potencias(9, 9)) # no se cumple teorema. Ver a=2

def tabla_genaralizacion_Euler(m, k):
    tabla = tabla_potencias(m, k)
    encabezados1 = [f'a^{k}' for k in range(1, nt.totient(m))]
    encabezados2 = ["a^Phi(m)"]
    encabezados3 = [f'a^{k}' for k in range(nt.totient(m), k)]
    new_columns = encabezados1 + encabezados2 + encabezados3
    tabla.columns = new_columns
    return tabla

print(tabla_genaralizacion_Euler(14,14))
