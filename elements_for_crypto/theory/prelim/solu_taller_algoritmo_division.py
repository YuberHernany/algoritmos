import numpy as np
from time import time
import matplotlib.pyplot as plt

def algo_div_using_rationals(a, b):
    rational = a / b
    quotient = int(np.floor(rational))
    residue = a - b*quotient
    return quotient, residue

def algo_div_using_integers(a, b):
    if a < b:
        quotient = 0
        residue = a
    else:
        quotient = 1
        residue = a - b*quotient
        while residue >= b:
            quotient += 1
            residue = a - b*quotient
    return quotient, residue

def time_spend_using_rationals(a, b):
    init_time = time()
    q, r = algo_div_using_rationals(a, b)
    end_time = time()
    return end_time - init_time

def time_spend_using_integers(a, b):
    init_time = time()
    q, r = algo_div_using_integers(a, b)
    end_time = time()
    return end_time - init_time


if __name__ == "__main__":


    times_with_rationals = []
    times_with_integers = []
    
    for i in range(1000000, 55000000, 1000000):
        a = np.random.randint(10*(i+10), 10*(i+20))
        b = np.random.randint(10*(i), 10*(i+1))
        # b = 11113 # Phenomenon wired
        times_with_rationals.append(time_spend_using_rationals(a, b))
        times_with_integers.append(time_spend_using_integers(a, b))
    
    fig, ax = plt.subplots()
    ax.plot(times_with_rationals, '-o', label="times with rationals")
    ax.plot(times_with_integers, '-^', label='times with integers')
    ax.set_title("Times for division algorithm")
    plt.legend()
    plt.show()

    # init_time = time()
    # q, r = algo_div_using_rationals(a, b)
    # end_time = time()
    # print("quotient: ", q, ". \t", "residue: ", r)
    # difference1 = end_time - init_time
    # print("time with algo_div_using_rationals: ", difference1)

    # init_time = time()
    # q, r = algo_div_using_integers(a, b)
    # end_time = time()
    # print("quotient: ", q,". \t", "residue: ", r)
    # difference2 = end_time - init_time
    # print("time with algo_div_using_integers: ", difference2)

    # print("")
    # print(f"using rationals spends {difference1 / difference2} the time used with integers")

    