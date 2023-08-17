import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from crypto_Cesar import *
from tools_for_letters import *

alphabet = list('abcdefghijklmnñopqrstuvwxyz')
alphabet += [' ']
N = len(alphabet)
FRECUENTE = 'e'
POS_FRECUENTE = alphabet.index(FRECUENTE)


# mensaje = "gnglgñrnqguukñrng" # opcional
mensaje = """jqncbñwofqbncubñcvgñcvkecubtgswktgobñwejcbñwejcbfkuekrnkoc"""


conteo_de_letras = Counter(mensaje) # this is a dict
datos = pd.Series(conteo_de_letras)
frec_maxima = np.max(datos)
letra_mas_frecuente = [key for key, value in conteo_de_letras.items() if value == frec_maxima][0]
pos_letra_mas_frecuente = alphabet.index(letra_mas_frecuente)
clave_potencial_de_encrip = abs(POS_FRECUENTE - pos_letra_mas_frecuente)
clave_potencial_de_desencrip = N - clave_potencial_de_encrip

if __name__ == "__main__":
    
    numeric = message2list_of_digits(mensaje)
    hack = encrypt_Cesar(numeric, clave_potencial_de_desencrip)
    lista = list_of_digits2message(hack)
    my_string = ""
    for letra in lista:
        my_string += letra

    print(my_string)
