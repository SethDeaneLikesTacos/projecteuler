import pef
import time
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

def main():
    start_time = time.time()

    i = 1
    count = 1
    while count < 10001:
        i += 1
        if pef.isprime(i):
            count += 1

    end_time = time.time()
    pef.answer(i, end_time - start_time)

main()
