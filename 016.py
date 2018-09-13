import pef
import time
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
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