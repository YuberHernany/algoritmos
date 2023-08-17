# all the tools are for transform message to list of integers (blocks)

import numpy as np
import sympy.ntheory as nt
import sympy as sy

alphabet = list('abcdefghijklmnñopqrstuvwxyz')
N = len(alphabet)
alphabet += [' ']
numbers = list(11 + np.arange(N)) + [38]

DICT = {letter:number for letter, number in zip(alphabet, numbers)}
DICT_INV = {number:letter for letter, number in zip(alphabet, numbers)}

def message2digits(message):
    """INPUTS: message (str)
      OUTPUTS: digits_str (str)"""
    digits_list = [str(DICT[letter]) for letter in message]
    digits_str = ""
    for string in digits_list:
        digits_str += string
    return digits_str

def regular_blocks(digits_str, possible_len=4):
    L = possible_len
    my_blocks = []
    n = len(digits_str) // L
    for i in range(n):
        my_blocks.append(digits_str[L*i:L*(i+1)])
    return my_blocks

def join_blocks_starting_with_zero(blocks):
    """INPUTS: blocks (list of strings_of_digits)
       OUTPUTS: (list) of string_of_digits that don't start with zero"""
    new_blocks = [blocks[0]]
    for block in blocks[1:]:
        if block[0] != '0':
            new_blocks.append(block)
        else:
            new_blocks[-1] += block
    return new_blocks

def blocks_like_str(digits_str, possible_len=4):
    reg_blocks = regular_blocks(digits_str, possible_len=possible_len)
    my_blocks = join_blocks_starting_with_zero(reg_blocks)
    return my_blocks

def blocks_like_int(my_blocks_like_str):
    return [int(block) for block in my_blocks_like_str]

def message2blocks(message, possible_len=4):
    digits_str = message2digits(message)
    my_blocks_str = blocks_like_str(digits_str, possible_len=possible_len)
    my_blocks_int = blocks_like_int(my_blocks_str)
    return my_blocks_int


if __name__ == "__main__":
    pass