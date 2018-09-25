import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=24
"""


elements = 10
number = 1000000

def main():

    num_array = []  # numerator digits
    den_array = []  # denominator digits
    fac_array = []  # factorial digits (this is what we translate to decimal)
    ava_array = []  # available numbers to use in the decimal form
    dec_array = []  # where the final output is stored

    # fill arrays
    for i in range(elements):
        den_array.append(math.factorial(i))
        num_array.append((number - 1) % math.factorial(i+1))
        fac_array.append(num_array[i] // den_array[i])
        ava_array.append(i)

    # find decimal value
    for i in range(elements-1, -1, -1):
        dec_array.append(ava_array[fac_array[i]])
        ava_array[fac_array[i]] = elements
        ava_array = sorted(ava_array)

    return ''.join(str(e) for e in dec_array)


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
