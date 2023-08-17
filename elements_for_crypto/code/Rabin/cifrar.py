# all the tools are for transform message to list of integers (blocks)
from tools_for_Rabin import *
from sympy.ntheory.modular import crt
import numpy as np
import sympy.ntheory as nt
import sympy as sy

alphabet = list('abcdefghijklmnñopqrstuvwxyz')
N = len(alphabet)
alphabet += [' ']
numbers = list(11 + np.arange(N)) + [38]

DICT = {letter:number for letter, number in zip(alphabet, numbers)}
DICT_INV = {number:letter for letter, number in zip(alphabet, numbers)}

def message2digits_str(message):
    """INPUTS: message (str)
      OUTPUTS: digits_str (str)"""
    digits_list = [str(DICT[letter]) for letter in message]
    digits_str = ""
    for string in digits_list:
        digits_str += string
    return digits_str

def jacobi_cut(digits_str, n):
    """INPUTS: digits_str (str), n (int)
     OUTPUTS: tuple of strings (str1, str2) where int(str1) 
                has jacobi symbols 1 mod n"""
    I_can_cut = False
    i = 1
    while not I_can_cut:
        num_left = int(digits_str[:i])
        if sy.ntheory.jacobi_symbol(num_left, n) == 1:
            I_can_cut = True
        i += 1
    return digits_str[:i-1], digits_str[i-1:]

def jacobi_cuts(digits_str, n):
    """INPUTS: digits_str (str), n (int)
     OUTPUTS: list of ints. Each int has jacobi symbols 1 mod n"""
    list_cuts = []
    b1, b2 = jacobi_cut(digits_str, n)
    list_cuts.append(int(b1))
    list_cuts.append(b2)
    while len(list_cuts[-1]) > 6:
        b1, b2 = jacobi_cut(list_cuts[-1], n)
        list_cuts.append(int(b1))
        list_cuts.append(b2)
    integers = [b for b in list_cuts if type(b) == type(3)] + [int(b2)]
    return integers

def encrypt_Rabin(blocks, n):
    """INPUTS: blocks (list of ints ciphered) where each b has jacobi symbols 1
                n (int)
     OUTPUTS: encrypted (list of ints), squares of the elements of blocks"""
    encrypted = [pow(b, 2, n) for b in blocks]
    return encrypted

def decrypt_Rabin(encrypted, p, q): # using chinese remainder therorem
    # I need to explore how get the small number < (p*q // 2) and jacobi_syb 1 in crt
    """INPUTS: encrypted (list of ints), p and q, (ints) primes conguents with 3 mod 4
     OUTPUTS: blocks (list of ints)"""
    u_s = [pow(a, (p+1)//4, p) for a in encrypted]
    v_s = [pow(a, (q+1)//4, q) for a in encrypted]
    x_s = [int(crt([p, q], [u, v])[0]) % (p*q) for u, v in zip(u_s, v_s)]
    return x_s # it doesn't work

def decrypt_Rabin2(encrypted, p, q): # without the use of chinese remainder theorem
    """INPUTS: encrypted (list of ints), p and q, (ints) primes conguents with 3 mod 4
     OUTPUTS: blocks (list of ints)"""
    all_roots = [sy.ntheory.sqrt_mod(a, p*q, True) for a in encrypted]
    all_roots_small = [[b for b in roots if b < ((p*q // 2))] for roots in all_roots]
    roots_jacobi1 = [[b for b in roots if sy.ntheory.jacobi_symbol(b, p*q) == 1][0] for roots in all_roots_small]
    return roots_jacobi1 # it doesn't work

# def jacobi_slice(digits_str, n):
#     current_idx = 0
#     len_substring = 2
#     blocks = []
#     current_int = int(digits_str[current_idx:current_idx + len_substring])
#     while sy.ntheory.jacobi_symbol(current_int, n) == -1:
#         len_substring += 1
#         current_int = int(digits_str[current_idx:current_idx + len_substring])
#     current_int.append(blocks)



# def message2digits_list(message):
#     digits_str = message2digits_str(message)
#     return [int(n) for n in list(digits_str)]

# def concatenate_pair(blocks, n):
#     """INPUTS: blocks (list of ints). n (int)
#     OUTPUTS: new_blocks (list of ints)"""
#     new_blocks = blocks.copy()
#     for i, b in enumerate(blocks):
#         if sy.ntheory.jacobi_symbol(b, n) == -1:
#             index = i
#             break
#     num_left_str = str(blocks[index])
#     num_right_str = str(blocks[index+1])
#     new_num = int(num_left_str + num_right_str)
#     new_blocks[index: index + 2] = [new_num]
#     return new_blocks

# def jacobi_symbols_of(blocks, n):
#     return [sy.ntheory.jacobi_symbol(b, n) for b in blocks]

# def concatenate_pairs(blocks, n):
#     new_blocks = blocks.copy()
#     while -1 in set(jacobi_symbols_of(new_blocks, n)):
#         new_blocks = concatenate_pair(new_blocks, n)
#     return new_blocks


if __name__ == "__main__":
    ############## problemas, estan apareciendo bloque muy grandes, ademas se tiene una salida aleatoria
    # p, q = two_big_primes_res3mod4(10000)
    p, q =  2459, 2467
    n = p * q
    # numbers = list(range(11, 38)) * 2
    # print(numbers)
    # print(len(numbers))
    # final = concatenate_pairs(numbers, n)
    # print(final)
    # print(n)
    message = 'teamoteamoteamo' # hay valores para los que no funciona
    
    my_digits_str = message2digits_str(message)
    print(my_digits_str)
    my_list =  jacobi_cuts(my_digits_str, n)
    print(my_list)
    # jacobi_symbols = [sy.ntheory.jacobi_symbol(b, n) for b in my_list]
    # print(jacobi_symbols)
    my_encrypted = encrypt_Rabin(my_list, n)
    print(my_encrypted)
    my_decrypted = decrypt_Rabin2(my_encrypted, p, q)
    print(my_decrypted)
    pass