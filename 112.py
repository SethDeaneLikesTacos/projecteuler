import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=112
5.284278869628906
"""


def main():


    cntBncy = 0                         # count of numbers that are bouncy
    i = 0                               # current number to test for bounciness
    percentBncy = 0                     # percent of numbers that are bouncy

    while percentBncy < 0.99:
        i += 1                          # increment number being checked

        ilst = [int(d) for d in str(i)] # break current number into list of digits
        pos = False                     # flag for ascending numbers
        neg = False                     # flag for descending numbers

        # run through each pair of two digits and see if we have an ascending
        # and descending pair
        for j in range(len(ilst)-1):
            if ilst[j] > ilst[j+1]: pos = True
            if ilst[j] < ilst[j+1]: neg = True
            
            # If we have both an ascending and descending pair,
            # then we have a bouncy number.
            if pos and neg:
                cntBncy += 1
                break
        
        percentBncy = cntBncy/i         # calculate bouncy percentage
    return i


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
