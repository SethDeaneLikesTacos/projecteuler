import resources.pef as pef
import time
"""
https://projecteuler.net/problem=46
33.6919801235199
"""


def main():

    i = 1
    while True:

        # use only odd numbers
        i += 2

        # if i is prime, then loop again
        if (pef.is_prime(i)):
            continue

        # set our variable to see if we make it through all combinations without
        # finding a matching set
        check = False

        # otherwise, see if we can find an exception
        for j in range(i, 0, -1):
            if (pef.is_prime(j)):

                k = 1
                # only need to check the answer if its going to be less than i
                while j + (2 * (k**2)) <= i:

                    if (i == j + (2 * (k**2))):
                        check = True

                    k += 1

        # check if we've found the appropriate number
        if check == False:
            return i


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
