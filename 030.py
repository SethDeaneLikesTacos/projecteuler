import resources.pef as pef
import time
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
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
