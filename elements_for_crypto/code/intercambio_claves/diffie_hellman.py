# programa para practicar el intercambio de claves Diffie-Hellman

import sympy.ntheory as nt
import random
from rsa import pow_a_mod, alfabeto, texto_a_num, particion, consigue_letras
# se elige un numero primo grande
"""
p = nt.prime(10000)
g = nt.primitive_root(p)
clave_publica = [p,g]
m_Dan = random.randint(1,10000)
n_Hellen = random.randint(1,10000)
# debe hellen comunicar a dan g**n mod p
valor_que_manda_Hellen = pow_a_mod(g, n_Hellen, p)
valor_que_manda_Dan = pow_a_mod(g, m_Dan, p)

clave = pow_a_mod(valor_que_manda_Dan, n_Hellen, p)


print(p)
print(n_Hellen)
print(m_Dan)
print(g)
print('________________________________')
print("la clave compartida es: ")
print("________________________")
print(clave)
"""

# ahora quiero verificar cuentas ElGamal con un ejemplo concreto que despues, debo encapsular con clases, metods, funciones, documentacion

p = 29
g = nt.primitive_root(p)
print(g)
e = 22 #este numero es la clave secreta de usuario A que luego recibira un mensaje desde usuario B
a = pow_a_mod(g,e,p) # clave publica de usuario A
print(a)
mensaje = 'algo' # mensaje que otro usuario B querra mandar al usuario A
B = texto_a_num(mensaje)
print(B)
bloques = particion(B,2) #bloques de numero todos menores que el primo p
print(bloques)
k = 3 # este numero lo puede escoger a su gusto el usuario B
gamma = pow_a_mod(g,k,p)
print(gamma)
a_alak = pow_a_mod(a,k,p) #factor con el cual cada bloque b en bloques sera encriptado
mensaje_encriptado = []
for bloque in bloques:
    mensaje_encriptado.append((a_alak * int(bloque)) % p)
print(mensaje_encriptado)
tuplas_a_mandar = []
for parte in mensaje_encriptado:
    tuplas_a_mandar.append((gamma,parte))
print(tuplas_a_mandar)
# a continuacion lo que tiene que hacer A para desenciptar el mensaje ='algo' que le ha enviado B
gamma_ala_menos_e_Factor_desencriptador = pow_a_mod(gamma, p-1-e, p)
print(gamma_ala_menos_e_Factor_desencriptador)
mensaje_original_recuperado =[]
for bloque in mensaje_encriptado:
    mensaje_original_recuperado.append((gamma_ala_menos_e_Factor_desencriptador * bloque) % p)
print(mensaje_original_recuperado)