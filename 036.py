import resources.pef as pef
import time
"""
https://projecteuler.net/problem=36
1.1346309185028076
"""

maximum = 1000000

def main():

    total = 0
    for i in range(maximum):

        # get the binary forward and reversed string representation of current number
        i_bin_for = str(bin(i))[2::]
        i_bin_rev = i_bin_for[::-1]

        # get the decimal forward and reversed string representation of current number
        i_dec_for = str(i)
        i_dec_rev = i_dec_for[::-1]

        if i_bin_for == i_bin_rev and i_dec_for == i_dec_rev:
            total += int(i_dec_for)

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
