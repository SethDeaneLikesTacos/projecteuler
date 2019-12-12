import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=28
0.00042128562927246094
"""


dim = 1001

def main():

    total = 1   # total sum thus far
    count = 1   # current number along the diagonal
    diff = 2    # the length difference between corners of the box

    for i in range( math.floor(dim/2) * 4):

        count += diff
        if i % 4 == 3:
            diff += 2
        total += count

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
    
