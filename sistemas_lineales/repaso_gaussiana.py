import numpy as np

def escalonar(A_b):
    m, n = A.shape # capturo cantidad de filas y cantidad de cols
    U_c = A_b.copy() # creo una copia 
    for j in range(n):
        for i in range(j+1, m):
            U_c[i, j:] -= (U_c[i,j] / U_c[j,j]) * U_c[j, j:]
    U, c = U_c[:, :-1], U_c[:, -1]
    return U, c


A = np.array([[1,1,1,1],
              [1,4,2,3],
              [4,7,8,9]], dtype=np.float64)
print(escalonar(A))


A = np.fromfunction(lambda i,j: 2*(i==j)+(-1)*(np.abs(i-j)==1), (10,10), dtype=np.float64)
b = np.eye(10)[1].reshape(-1,1) # debe ser una matriz columna para concatenar
A_b = np.hstack([A, b])
print(A_b)

print(escalonar(A_b)[0].round(2))