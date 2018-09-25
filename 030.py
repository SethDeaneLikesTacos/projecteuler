import resources.pef as pef
import time
"""
https://projecteuler.net/problem=30
"""


def filldigits(n):
    digits = []
    strn = str(n)
    for i in strn:
        digits.append(int(i))
    return digits


def main():

    total = []
    for i in range(2, 200000):
        digits = filldigits(i)
        for d in range(len(digits)):
            digits[d] = digits[d] ** 5
        if sum(digits) == i:
            total.append(i)

    return sum(total)

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
