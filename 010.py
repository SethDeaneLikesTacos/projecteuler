import pef
import time
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def main():
    start_time = time.time()

    total = sum(pef.prime_sieve(0, 2000000))

    end_time = time.time()
    pef.answer(total, end_time - start_time)

main()
