import resources.pef as pef
import time
import itertools
"""
https://projecteuler.net/problem=49
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
                    pef.is_prime(j) and pef.is_prime(k) and \
                    i != 1487:

                    return ''.join(str(i) + str(j) + str(k))


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
