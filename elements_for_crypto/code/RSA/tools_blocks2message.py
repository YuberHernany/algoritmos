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
    """INPUTS: digits_str (str) whose characters are digits
      OUTPUTS: message (str) whose characters are letter from alphabet
    """
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
    message = digits2message(my_digits_str)
    return message
    
if __name__ == "__main__":
    # my_blocks = ['11', '12', '13', '14']
    # print(type(unified_string(my_blocks)))
    # print(digits2message('111213141112131411121314'))
    # print(blocks2message(my_blocks))
    pass

