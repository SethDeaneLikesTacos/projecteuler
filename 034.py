import resources.pef as pef
import time
from math import factorial
"""
https://projecteuler.net/problem=34
"""


def main():

    total = 0
    for i in range(3, 50000):
        l = [int(j) for j in str(i)]

        tot = 0
        for k in l:
            tot += factorial(k)
            if tot == i:
                total += i

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
