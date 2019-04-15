import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=44
"""


def main():

    not_found = True

    i = 1
    while not_found:
        i += 1

        Pn = i * (3 * i - 1) / 2
        for j in range(1, i):
            Pp = j * (3 * j - 1) / 2
            if (pef.is_shape(abs(Pn - Pp), 5) and \
                pef.is_shape(abs(Pn + Pp), 5)):

                return int(abs(Pn - Pp))


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
