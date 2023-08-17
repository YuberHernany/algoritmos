import numpy as np
import pandas as pd
import sympy.ntheory as nt
from sympy import igcd

def tabla_potencias(m, k):
    """m: int, modulo. k:int, max potencia """
    arr = np.fromfunction(lambda i,j: (((i+1)**(j+1))%m)*((i+1)*(j+1)>=1), (m-1,k), dtype=int)
    tabla = pd.DataFrame(arr,
                         columns=[f'a^{k}' for k in range(1, k+1)],
                         index=[k for k in range(1, m)])
    return tabla

# print(tabla_potencias(9, 9)) # no se cumple teorema. Ver a=2

def tabla_genaralizacion_Euler(m, k):
    tabla = tabla_potencias(m, k)
    phi_m = nt.totient(m)
    encabezados1 = [f'a^{k}' for k in range(1, phi_m - 1)]
    encabezados2 = [f"a^Phi({m})-1", f"a^Phi({m})"]
    encabezados3 = [f'a^{k}' for k in range(phi_m + 1, k+1)]
    new_columns = encabezados1 + encabezados2 + encabezados3
    tabla.columns = new_columns
    return tabla.T[::-1]
    

if __name__ == "__main__":

    # for p in nt.primerange(2, 10):
    #     print(tabla_potencias(p, p))

    # for p in range(2,10):
    #     print(tabla_genaralizacion_Euler(p,p))

    # print(tabla_potencias(7, 7))
    print(tabla_genaralizacion_Euler(7,7))