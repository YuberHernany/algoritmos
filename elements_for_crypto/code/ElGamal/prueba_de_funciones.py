from crypto_ElGamal_new import *
from tools_message2blocks import *
from tools_blocks2message import *
import sympy.ntheory as nt

if __name__ == "__main__":
    # # A quiere que recibir mensajes. Toma clave privada e
    # # y hace pública la clave (p, g, a) con a = pow(g, e, p)
    # e = 2

    # # B quiere mandar mensaje a A (B tiene clave pública de A: (p, g, a))
    # message = 'elgamalesuncriptosistemadeclavepublica'
    # cipher = message2blocks(message, possible_len=2)
    # print(cipher)
    # # p, g, a = 79, 3, 9 # otra opcion
    # # p, g, a = 1000003, 2, 4 # ejemplo para usar con possible_len=6
    # p, g, a = 7919, 7, 49 # recordar 49 = pow(g, e, p) = pow(7, 2, 7919)
    # k = 3
    # gam = pow(g, k, p)
    # fac_enc = pow(a, k, p)
    # print("factor for encrypt: ", fac_enc)
    # encrypted = [(fac_enc * b) % p for b in cipher]
    # print("encrypted: ", encrypted)
    # fac_dec = pow(gam, p-1-e, p)
    # print("factor for decrypt: ", fac_dec)
    # decrypted = [(fac_dec * beta) % p for beta in encrypted]
    # print('decrypted: ', decrypted)
    # message_revisited = blocks2message(decrypted)
    # print("mensaje orginal desencriptado: ")
    # print(message_revisited)

    # ###################################################################
    # # Now we will test the task using functions from crypto_ELGamal_new
    # # A quiere que recibir mensajes. Toma clave privada e
    # # y hace pública la clave (p, g, a) con a = pow(g, e, p)
    # e = 2

    # # B quiere mandar mensaje a A (B tiene clave pública de A: (p, g, a))
    # message = 'elgamalesuncriptosistemadeclavepublica'
    # cipher = message2blocks(message, possible_len=2)
    # print(cipher)
    # # p, g, a = 79, 3, 9 # otra opcion
    # # p, g, a = 1000003, 2, 4 # ejemplo para usar con possible_len=6
    # p, g, a = 7919, 7, 49 # recordar 49 = pow(g, e, p) = pow(7, 2, 7919)
    # k = 3
    # gam = pow(g, k, p)
    # fac_enc = pow(a, k, p)
    # print("factor for encrypt: ", fac_enc)
    # gam, encrypted = encrypt_ElGamal_with_k_prefixed(cipher, p, g, a, k)
    # print("gamma: ", gam)
    # print("encrypted: ", encrypted)
    # fac_dec = pow(gam, p-1-e, p)
    # print("factor for decrypt: ", fac_dec)
    # decrypted = decrypt_ElGamal_new(encrypted, p, g, a, e, gam)
    # print('decrypted: ', decrypted)
    # message_revisited = blocks2message(decrypted)
    # print("mensaje orginal desencriptado: ")
    # print(message_revisited)

    #########################################################################
    # with signature
    # A quiere que recibir mensajes. Toma clave privada e
    # y hace pública la clave (p, g, a) con a = pow(g, e, p)
    e = 2

    # Lo que hace B
    # B quiere mandar mensaje a A (B tiene clave pública de A: (p, g, a))
    message = 'elgamalesuncriptosistemadeclavepublica'
    cipher = message2blocks(message, possible_len=2)
    # print(cipher)
    # # p, g, a = 79, 3, 9 # otra opcion
    # # p, g, a = 1000003, 2, 4 # ejemplo para usar con possible_len=6
    p, g, a = 7919, 7, 49 # recordar 49 = pow(g, e, p) = pow(7, 2, 7919)
    k = 3
    gam = pow(g, k, p)
    fac_enc = pow(a, k, p)
    # print("factor for encrypt: ", fac_enc)
    gam, encrypted = encrypt_ElGamal_with_k_prefixed(cipher, p, g, a, k)
    # print("gamma: ", gam)
    # print("encrypted: ", encrypted)
    # Lo que sigue haciendo B si desea firmar
    e_hat_ = 7 # privada de B
    a_hat_ = pow(g, e_hat_, p) # B esconde su privada e_hat_
    k_inv = pow(k, nt.totient(p)-1, p) # se necesita para signature s
    s = ((cipher[0] - e_hat_ * gam) * k_inv) % p # only s for b1 = cipher[0]
    signa = (s, a_hat_)
    messa_enc = (gam, encrypted[0])
    print(signa, messa_enc)



    # Lo que hace A para recibir mensaje y firma
    fac_dec = pow(gam, p-1-e, p)
    # print("factor for decrypt: ", fac_dec)
    decrypted = decrypt_ElGamal_new(encrypted, p, g, a, e, gam)
    b = decrypted[0]
    V1 = (pow(gam, s, p) * pow(a_hat_, gam, p)) % p
    V2 = pow(g, b, p)
    print("V1: ", V1)
    print("V2: ", V2)
    # se supone que deben ser iguales V1 y V2
    
    # print('decrypted: ', decrypted)
    # message_revisited = blocks2message(decrypted)
    # print("mensaje orginal desencriptado: ")
    # print(message_revisited)
    pass