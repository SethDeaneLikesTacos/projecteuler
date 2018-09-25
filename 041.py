import resources.pef as pef
import time
"""
https://projecteuler.net/problem=41

NOTE: This one takes a long time :/
"""


def main():

    maxprime = 0
    primes = set(pef.prime_sieve(99999999))
    for i in primes:
        if pef.is_pandigital(i, len(str(i))):
            maxprime = i

    return maxprime


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
