import pef
import time
import math
"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations
of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

elements = 10
number = 1000000

def main():
    start_time = time.time()

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

    # print answer
    end_time = time.time()
    pef.answer(''.join(str(e) for e in dec_array), end_time - start_time)

main()
