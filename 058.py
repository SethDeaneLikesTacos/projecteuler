import resources.pef as pef
import time
"""
https://projecteuler.net/problem=58
"""


def main():

    total_primes = 0

    dist = 0
    cur = 1
    for i in range(100000):

        cur += dist

        # check the ratio of primes
        if i > 10:
            ratio = total_primes / i
            if ratio <= .1:
                return dist + 1

        # if ratio of primes 
        if pef.is_prime(cur):
            total_primes += 1

        # increment the distance
        if i % 4 == 0:
            dist += 2


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
