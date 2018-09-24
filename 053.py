import resources.pef as pef
import time
from math import factorial as fac
"""
https://projecteuler.net/problem=53
"""


def ncr(n, r):
    return fac(n) / (fac(r) * fac(n-r))


def main():
    total = 0
    for i in range(1, 101):
        for j in range(1, i+1):
            if ncr(i,j) >= 1000000:
                total+=1

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
