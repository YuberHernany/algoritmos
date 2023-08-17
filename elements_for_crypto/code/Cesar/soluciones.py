from tools_for_letters import *
from crypto_Cesar import *
from sympy.core import igcd
import sympy.ntheory as nt

############################################################################
# # ejercicio 1)
# mensaje = "casa con dos puertas"
# print("quiero encriptar usando k = 7 en cifrado cesar: ", mensaje)
# my_list_ints = message2list_of_digits(mensaje)
# print("texto plano corresponde a : ", my_list_ints)
# k = 7
# my_encrypted_nums = encrypt_Cesar(my_list_ints, k)
# print("resultado de encriptar en números: ", my_encrypted_nums)
# my_encrypted_str = list_of_digits2message(my_encrypted_nums)
# print("mensaje encriptado: ", my_encrypted_str)

############################################################################
# ejercicio 2)
encriptado = "btoclyzkhk"
k = 7
clave_para_desencriptar = get_key_for_decrypt(k)
print("la clave para desencriptar es: ", clave_para_desencriptar)
my_list_ints = message2list_of_digits(encriptado)
print("texto cifrado corresponde a : ", my_list_ints)
desencriptado = decrypt_Cesar(my_list_ints, clave_para_desencriptar)
desencriptado_str = list_of_digits2message(desencriptado)
print("El mensaje descrifrado es: ", desencriptado_str)

############################################################################
# ejercicio 3) 
# def encrypt_Cesar_afin(list_of_ints, a_key, k_key):
#     """INPUTS: list_of_ints (list). a_key, k_key (int)
#      OUTPUTS: encrypted_num (list)"""
#     encrypted_num = []
#     N = len(alphabet)
#     if igcd(a_key, N) == 1:
#         encrypted_num = [(a_key * num + k_key) % N for num in list_of_ints]
#     else:
#         print('la clave a_key no es válida')
#     return encrypted_num

# def get_keys_for_decrypt_afin(a_key, k_key):
#     """INPUTS: a_key, k_key (ints)
#      OUTPUTS: a_dekey, k_dekey (ints)"""
#     N = len(alphabet)
#     k_dekey = N - k_key
#     a_dekey = pow(a_key, nt.totient(N) - 1, N)
#     return a_dekey, k_dekey

# def decrypt_Cesar_afin(list_of_ints, a_key, k_key):
#     """INPUTS: list_of_ints (list). a_key, k_key (int)
#      OUTPUTS: decrypted_num (list)"""
#     a_dekey, k_dekey = get_keys_for_decrypt_afin(a_key, k_key)
#     decrypted_num = encrypt_Cesar_afin(list_of_ints, a_dekey, k_dekey)
#     return decrypted_num

############################################################################
# ejercicio 4)
# usando C = 2T+5 mod 27, encripte ALGO

# def encrypt_Cesar_afin(list_of_ints, a_key, k_key):
#     """INPUTS: list_of_ints (list). a_key, k_key (int)
#     OUTPUTS: encrypted_num (list)"""
#     encrypted_num = []
#     N = len(alphabet)
#     if igcd(a_key, N) == 1:
#         encrypted_num = [(a_key * num + k_key) % N for num in list_of_ints]
#     else:
#         print('la clave a_key no es válida')
#     return encrypted_num

# mensaje = "algo"
# my_list_ints = message2list_of_digits(mensaje)
# a, k = 2, 5
# print(encrypt_Cesar_afin(my_list_ints, a, k))

if __name__ == "__main__":
    


    pass 
