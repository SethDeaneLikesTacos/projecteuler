import resources.pef as pef
import time
"""
https://projecteuler.net/problem=14
"""


def main():

    maxlen = 0

    for i in range(1000000, 1, -1):
        n = i
        l = 1

        while n > 1:
            l += 1
            if n % 2 == 0:
                n /= 2
            elif n % 2 == 1:
                n = 3 * n + 1

        if l > maxlen:
            maxlen = l
            maxstart = i

    return maxstart


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
