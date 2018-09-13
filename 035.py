import pef
import time
"""
The number, 197, is called a circular prime because
all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7,
11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


def rotate(num, amount):
    lnum = [int(j) for j in str(num)]

    for i in range(amount):
        lnum.append(lnum.pop(0))

    num = int(''.join(map(str,lnum)))
    return num


def main():

    primes = pef.prime_sieve(0, 1000000)

    count = 4
    for i in primes:
        primecount = 1
        for j in range(1, len(str(i))):

            num = rotate(i, j)

            if num in primes:
                primecount += 1
                if primecount == len(str(i)):
                    count += 1

    return count


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
