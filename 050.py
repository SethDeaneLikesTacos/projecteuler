import pef
import time
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


def main():
    maximum = 100
    primes = pef.prime_sieve(maximum)

    looping = True
    while looping:

        sum = 0
        longest = 0
        for p in primes:
            sum += p
            if pef.isprime(sum):
                return sum



if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
