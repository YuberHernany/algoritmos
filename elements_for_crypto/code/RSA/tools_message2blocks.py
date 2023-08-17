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
    """INPUTS: digits_str (str), possible_len (int) default 4
        OUTPUTS: list of strings whose characters are integers"""
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
    """INPUTS: digits_str (str) whose characters are digits
    OUTPUTS: list of strings whose characters are digits"""
    reg_blocks = regular_blocks(digits_str, possible_len=possible_len)
    my_blocks = join_blocks_starting_with_zero(reg_blocks)
    return my_blocks

def blocks_like_int(my_blocks_like_str):
    """INPUTS: my_blocks_like_str (list) of string whose characters are digits
        OUTPUTS: (list) of integers. That will be used for ecryption method"""
    return [int(block) for block in my_blocks_like_str]

def message2blocks(message, possible_len=4):
    digits_str = message2digits(message)
    my_blocks_str = blocks_like_str(digits_str, possible_len=possible_len)
    my_blocks_int = blocks_like_int(my_blocks_str)
    return my_blocks_int


if __name__ == "__main__":
    # print(alphabet)
    # print(type(alphabet))
    # print(numbers)
    # print(type(numbers))
    # print(len(alphabet) == len(numbers))
    # print(DICT)
    # print(DICT_INV)
    # print(message2digits("hola"))
    # print(type(message2digits('hola')))

    # long_string = message2digits("hola")
    # print(regular_blocks(long_string, possible_len=2))
    
    # my_blocks = ['11', '12', '13', '14']
    # my_blocks = ['11', '02', '13', '04']
    # my_blocks = ['11', '02', '13', '14']
    # print(join_blocks_starting_with_zero(my_blocks))

    # print(blocks_like_str("11121314"))
    # print(type(blocks_like_str("11121314")))
    # print(blocks_like_int(["11","12","13","14"]))
    # print(type(blocks_like_int(["11","12","13","14"])))

    # message = "hola mundo hello world este es mi mensaje"
    # print(message2blocks(message=message, possible_len=6))
    pass