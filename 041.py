import pef
import time
"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


def main():

    maxprime = 0
    primes = pef.prime_sieve(0, 99999999)
    for i in primes:
        if pef.is_pandigital(i, len(str(i))):
            maxprime = i

    return maxprime


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
