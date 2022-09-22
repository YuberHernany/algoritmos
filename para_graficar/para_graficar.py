import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
x = sy.symbols('x')

def ejes():
    ax = plt.gca()
    ax.spines['bottom'].set_position("zero")
    ax.spines['left'].set_position("zero")

def graficar(f, dominio, **kwargs):
    ax = plt.gca()
    F = sy.lambdify(x, f, "numpy")
    x_s = np.linspace(dominio[0], dominio[1])
    ax.plot(x_s, F(x_s), **kwargs)

if __name__ == "__main__":
    pass 