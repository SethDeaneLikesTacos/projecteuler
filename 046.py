import pef
import time
"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""


def main():

    i = 1
    while True:

        # use only odd numbers
        i += 2

        # if i is prime, then loop again
        if (pef.isprime(i)):
            continue

        # set our variable to see if we make it through all combinations without
        # finding a matching set
        check = False

        # otherwise, see if we can find an exception
        for j in range(i, 0, -1):
            if (pef.isprime(j)):

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
