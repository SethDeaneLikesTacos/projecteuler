import resources.pef as pef
import time
"""
https://projecteuler.net/problem=50
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
                pef.is_prime(sum(inq)):
                dic['len'] = len(inq)
                dic['num'] = sum(inq)

    return dic['num']



if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
