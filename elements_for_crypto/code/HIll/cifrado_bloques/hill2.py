import numpy as np
import sympy.ntheory as nt
from sympy.core import igcd
import re

alphabet = 'abcdefghijklmnñopqrstuvwxyz'
numbers = np.arange(len(alphabet))
DICT = {letter:number for letter, number in zip(alphabet, numbers)}
DICT_INV = {value:key for key, value in DICT.items()}

def letter_to_number_block_n(block_str):
    n = len(block_str)
    return np.array([DICT[s] for s in block_str]).reshape(-1,1)

def are_relative_primes(a, b):
    return igcd(a, b) == 1

def is_invertible(A, modulo=27):
    """verify if det(A) and modulo are relative primes"""
    D = int(np.round(np.linalg.det(A))) % modulo
    return are_relative_primes(D, modulo)

def inverse_modulo(A, modulo=27):
    if is_invertible(A):
        a, b, c, d = A[0,0], A[0,1], A[1,0], A[1,1]
        D = int(np.round(np.linalg.det(A))) % modulo
        D_inv = (D ** (nt.totient(modulo) - 1)) % modulo
        D_inv_neg = modulo - D_inv
        A_inv = np.array([[D_inv * d, D_inv_neg * b], 
                          [D_inv_neg * c, D_inv * a]]).astype(np.int64)
        A_inv = A_inv % modulo
        return A_inv
    else:
        print('The matrix is not invertible')

def complete_string(my_string):
    if len(my_string) % 2 == 0:
        return my_string
    else:
        return my_string + 'x'

def separate_string_in_blocks(my_string, length_block=2):
    new_string = complete_string(my_string)
    blocks = [new_string[k:k+length_block] for k in range(0, len(new_string)-1, length_block)]
    return blocks

def create_number_blocks(my_string, length_block=2):
    blocks_of_letters = separate_string_in_blocks(my_string, length_block=length_block)
    C = np.hstack([letter_to_number_block_n(block_str) for block_str in blocks_of_letters])
    return C

def encrypt_num(key, my_string, modulo=27):
    """key is matrix invertible modulo"""
    n_rows = len(key)
    C_num = create_number_blocks(my_string, length_block=n_rows)
    return (key @ C_num) % modulo

def num2letter(number):
    return DICT_INV[number]

def nums2letters(matrix):
    n_rows, n_cols = len(matrix), len(matrix.T)
    return np.array([[num2letter(matrix[i][j]) for j in range(n_cols)] for i in range(n_rows)])

def all_letters(matrix_of_letters):
    return matrix_of_letters.T.ravel()

def letters(matrix):
    matrix_of_letters = nums2letters(matrix)
    list_of_letters = all_letters(matrix_of_letters)
    message = ''
    for letter in list_of_letters:
        message += letter
    return message

def encrypt_hill(key, my_string, modulo=27):
    matrix = encrypt_num(key, my_string, modulo=modulo)
    return letters(matrix)

def dynamical_key(order=2):
    potential_key = np.random.randint(low=0, high=27, size=(order, order))
    while not is_invertible(potential_key):
        potential_key = np.random.randint(low=0, high=27, size=(order, order))
    return potential_key

def flatened_dynamical_key(matrix):
    return matrix.ravel()

def head_info(flattened_matrix):
    head = ""
    for num in flattened_matrix:
        head += np.random.choice(list(alphabet)) + str(num)
    return head + "_"

def encrypt_hill_info(key, my_string, modulo=27, order=2):
    head = head_info(flatened_dynamical_key(key))
    encrypt_message = encrypt_hill(key, my_string)
    return head + encrypt_message

def extract_number_from(my_string):
    numbers = [int(s) for s in re.findall(r'\d+', my_string)]
    return np.array([[numbers[0], numbers[1]],
                     [numbers[2], numbers[3]]]).astype(np.int32)

def decrypt_hill(my_string):
    index_cut = my_string.index("_")
    key = extract_number_from(my_string)
    key_inv = inverse_modulo(key)
    my_string_without_numbers = my_string[index_cut+1:]
    decrypted = encrypt_hill(key_inv, my_string_without_numbers)
    return decrypted

if __name__ == "__main__":
    pass 


# review because with 3block is not working

# key = dynamical_key(order=3)
# print('With the flatened key: ', flatened_dynamical_key(key))
# key_inv = inverse_modulo(key)
# message = 'tenecesitotenecesitotenecesito'
# encrypted_message = encrypt_hill(key, message)
# print("encrypted message: ", encrypted_message)
# decrypted_message = encrypt_hill(key_inv, encrypted_message)
# print("decrypted message: ", decrypted_message)
# print(head_info(flatened_dynamical_key(key)))
# print(letter_to_number_block_n('hola'))
# A = np.array([[2,4], [2,4]])
# A = np.array([[2,1], [6,7]])
# A_inv = inverse_modulo(A)
# A3 = np.array([[1,0,0],
#               [0,1,0], 
#               [0,0,26]])
# print(A)
# print(is_invertible(A))
# print(inverse_modulo(A))
# print(A @ inverse_modulo(A))
# print(complete_string('hola'))
# print(encrypt_hill(A, 'yaentendi'))
# print(encrypt_hill(A3, 'yaentendi'))

# example decrypting
# key = np.array([[4,5],[3,2]])
# print(inverse_modulo(key))
# key = np.array([[2,1],[6,7]])
# key_decript = inverse_modulo(key)
# sent = 'sñrtbñistj'
# sent = 'wouhqncrna'
# print(encrypt_hill(key_decript, sent))
# print(key_decript)
