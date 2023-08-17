import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

freqs = [16.78,11.96,8.69,8.37,7.88,7.01,6.87,4.94,4.80,4.15,3.31,2.92,2.76,2.12,1.54,1.53,0.92,0.89]

letters = ["E","A","O","L","S","N","D","R","U","I","T","C","P","M","Y","Q","B","H"]

my_series = pd.Series(freqs, index=letters)

x_marcador = np.array([0,0,1,1])
y_marcador = np.array([0,1,1,0])

if __name__ == "__main__":
    my_series.plot(kind='bar')
    ax = plt.gca()
    ax.set(xlim=(-1,19), ylim=(-1, 19))
    ax.set_ylabel("%")
    ax.set_title("Frecuencias de letras en texto genérico en español")
    plt.text(1, 18, "Alta frecuencia")
    plt.text(7, 9, "Media frecuencia")
    plt.text(13, 4, "Baja frecuencia")
    ax.plot(6 * x_marcador, 0.5 * y_marcador + 17, color='black')
    ax.plot(6 * x_marcador + 6, 0.5 * y_marcador + 8, color='black')
    ax.plot(6 * x_marcador + 12, 0.5 * y_marcador + 3, color='black')
    plt.savefig('frecuencias_letras.png')
    # plt.show()