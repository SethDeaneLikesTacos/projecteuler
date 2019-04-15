import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=45
"""


def main():

    i = 2
    while True:
        i += 1

        number = int((i * (i+1) ) / 2)
        if (pef.is_shape(number, 6) and pef.is_shape(number, 5) and number != 40755):

            return number


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
