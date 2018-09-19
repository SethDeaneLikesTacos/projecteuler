import pef
import time
import itertools
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""


def main():

    # generate primes from 1000 - 9999
    primes = pef.prime_sieve(9999)[168:]

    for i in primes:
        jk_list = [int(x) for x in str(i)]    # list format of i
        jk_list_itts = list(itertools.permutations(jk_list))

        for j in jk_list_itts:
            # convert list of ints to int
            j = int(''.join(map(str,j)))

            for k in jk_list_itts:
                # convert list of ints to int
                k = int(''.join(map(str,k)))

                if abs(i - j) == abs(j - k) and \
                    i != j != k and i < j < k and \
                    pef.isprime(j) and pef.isprime(k) and \
                    i != 1487:

                    return ''.join(str(i) + str(j) + str(k))


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
