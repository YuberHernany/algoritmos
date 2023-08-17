# herramientas para transformar letras en números
import numpy as np

alphabet = list('abcdefghijklmnñopqrstuvwxyz')
N = len(alphabet)

numbers = list(np.arange(N))

DICT = {letter:number for letter, number in zip(alphabet, numbers)}
DICT_INV = {number:letter for letter, number in zip(alphabet, numbers)}


def message2list_of_digits(message):
    """INPUTS: message (str)
      OUTPUTS: list of ints"""
    digits_list = [DICT[letter] for letter in message]
    return digits_list

def list_of_digits2message(list_of_digits):
    """INPUTS: list of digits is a list of ints
      OUTPUTS: full_str (str)"""
    list_of_letters = [DICT_INV[integer] for integer in list_of_digits]
    full_str = ""
    for letter in list_of_letters:
        full_str += letter
    return full_str


if __name__ == "__main__":
    
    pass
    
    