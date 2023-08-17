import numpy as np
import sympy.ntheory as nt
import sympy as sy

alphabet = list('abcdefghijklmnñopqrstuvwxyz')
N = len(alphabet)
alphabet += [' ']
numbers = list(11 + np.arange(N)) + [38]

DICT = {letter:number for letter, number in zip(alphabet, numbers)}
DICT_INV = {number:letter for letter, number in zip(alphabet, numbers)}

def unified_string(blocks):
    """INPUTS: blocks (list of ints)
      OUTPUTS: unified (str)"""
    blocks_str = [str(block) for block in blocks]
    unified = ""
    for block_str in blocks_str:
        unified += block_str
    return unified

def digits2message(digits_str):
    pairs_of_digits = [digits_str[i:i+2] for i in range(0, len(digits_str), 2)]
    letters = [DICT_INV[int(pair)] for pair in pairs_of_digits]
    message = ""
    for letter in letters:
        message += letter
    return message

def blocks2message(blocks):
    """INPUTS: blocks (list of ints)
      OUTPUTS: message (str)"""
    my_digits_str = unified_string(blocks)
    return digits2message(my_digits_str)
    
if __name__ == "__main__":

    pass