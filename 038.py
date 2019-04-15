import resources.pef as pef
import time
"""
https://projecteuler.net/problem=38
"""


def main():

    maximum = 0

    # initial number
    for i in range(1, 10000):
        num_str = ""

        # list to multiply against
        for j in range(1, 100):
            num_int = i * j
            num_str += str(num_int)

            # we only want to check pandigitality if its a 9 digit number
            if len(num_str) == 9:

                if int(num_str) > maximum and pef.is_pandigital(int(num_str)):
                    maximum = int(num_str)

    return maximum


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
