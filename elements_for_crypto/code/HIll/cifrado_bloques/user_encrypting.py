import numpy as np
import sympy.ntheory as nt
from sympy.core import igcd
from hill2 import *

if __name__ == "__main__":
    key = dynamical_key(order=2)
    key_inv = inverse_modulo(key)
    message = input("Write the message you want to encrypt: ")
    encrypted_message = encrypt_hill(key, message)
    encrypted_with_info = encrypt_hill_info(key, message, order=2)
    print("encrypted message with info: ", encrypted_with_info)
    decrypted_message = decrypt_hill(encrypted_with_info)
    print(decrypted_message)