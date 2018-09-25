import resources.pef as pef
import time
"""
https://projecteuler.net/problem=10
"""


def main():

    total = sum(pef.prime_sieve(2000000))

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
