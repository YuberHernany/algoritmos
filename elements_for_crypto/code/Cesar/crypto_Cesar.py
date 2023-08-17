from tools_for_letters import *

def encrypt_Cesar(plane_list_of_ints, key):
    """INPUTS: list of ints. key (int)
      OUTPUTS: list of ints"""
    N = len(alphabet)
    encrypted = [(n + key) % N for n in plane_list_of_ints]
    return encrypted

def decrypt_Cesar(cipher_list_of_ints, key_to_decrypt):
    """INPUTS: cipher_list_of_ints is list of ints. key_to_decrypt (int)
      OUTPUTS: list of ints meaning the numbers that correspond to plane text"""
    decrypted = encrypt_Cesar(cipher_list_of_ints, key_to_decrypt)
    return decrypted

def get_key_for_decrypt(key_for_encrypt):
    """INPUT: key_for_encrypt (int)
      OUTPUT: key_for_decrypt (int)"""
    N = len(alphabet)
    return N - key_for_encrypt

if __name__ == "__main__":
    pass