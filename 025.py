import resources.pef as pef
import time
"""
https://projecteuler.net/problem=25
"""


def fib(fibl):
    tmp = fibl[0] + fibl[1]
    fibl[1] = fibl[0]
    fibl[0] = tmp
    return fibl


def main():

    fibl = [1,1]
    for i in range(3, 5000):
        fibl = fib(fibl)
        nDigits = len(str(fibl[0]))
        if nDigits == 1000:
            break

    return i


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
