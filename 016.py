import resources.pef as pef
import time
"""
https://projecteuler.net/problem=16
"""


def main():

    a = 2 ** 1000
    b = str(a)
    c = []
    d = 0

    for digit in b:
        c.append(int(digit))

    for digit in c:
        d += digit

    return d


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
