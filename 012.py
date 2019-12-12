import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=12
4.4421679973602295
"""


def main():

    i = 0
    tri = 0
    divisorcount = 0

    while divisorcount*2 <= 500:
        i += 1
        divisorcount = 1
        tri += i
        for j in range(math.ceil(math.sqrt(tri)), 1, -1):
            if tri % j == 0:
                divisorcount += 1

    return tri


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
