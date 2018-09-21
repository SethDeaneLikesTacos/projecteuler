import resources.pef as pef
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
    maximum = 1000000
    primes = pef.prime_sieve(maximum)

    dic = {}
    dic['len'] = 0
    dic['num'] = 0

    for a in range(10):
        for b in range(a,maximum):
            inq = primes[a:b]   # array in question
            if sum(inq) > maximum:
                break

            if len(inq) > dic['len'] and sum(inq) > dic['num'] and \
                pef.isprime(sum(inq)):
                dic['len'] = len(inq)
                dic['num'] = sum(inq)

    return dic['num']



if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
