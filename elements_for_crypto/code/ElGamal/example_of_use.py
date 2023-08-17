# from crypto_ElGamal import *
from tools_message2blocks import *
from tools_blocks2message import *
from crypto_ElGamal_new import *
import sympy.ntheory as nt

if __name__ == "__main__":
    message = 'elamorylasmatematicas'
    print(message) 
    e = 2
    # p, g, a = 29, 2, 5 # cuidado puesto que 29 es primo menor que algunos valores de diccionario
    p, g, a = 79, 3, 9
    k = 3 # it must be between 1 and p-2
    my_blocks = message2blocks(message, possible_len=2)
    print(my_blocks)
    gam, my_encrypted = encrypt_ElGamal_with_k_prefixed(my_blocks, p, g, a, k)
    print(my_encrypted)
    my_decrypted = decrypt_ElGamal(my_encrypted, p, g, a, e, k)
    print(my_decrypted)
    original_message = blocks2message(my_decrypted)
    print(original_message)
    pass