import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
x = sy.symbols('x')

def ejes():
    ax = plt.gca()
    ax.spines['bottom'].set_position("zero")
    ax.spines['left'].set_position("zero")

def graficar(f, dominio, **kwargs):
    """Entradas:
            f: expresión de sympy
            dominio: lista o array [star, stop] o [star, stop, steps]"""
    ax = plt.gca()
    F = sy.lambdify(x, f, "numpy")
    if len(dominio) == 2:
        x_s = np.linspace(dominio[0], dominio[1])
        ax.plot(x_s, F(x_s), **kwargs)
    elif len(dominio) == 3:
        x_s = np.linspace(dominio[0], dominio[1], dominio[2])
        ax.plot(x_s, F(x_s), **kwargs)
    
if __name__ == "__main__":
    pass 