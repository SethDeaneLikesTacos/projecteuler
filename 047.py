import resources.pef as pef
import time
"""
https://projecteuler.net/problem=47
"""


def number_unique_prime_factors(number, primes):
    not_completely_factored = True
    i = 0
    factors = []
    while not_completely_factored:

        if ( number / primes[i] == int(number / primes[i]) ):
            number = number / primes[i]
            factors.append(primes[i])
            i = -1

        if pef.isprime(number):
            not_completely_factored = False
            factors.append(int(number))
        i += 1

    return len(set(factors))


def main():

    how_many_primes = 500000
    primes = pef.prime_sieve(how_many_primes)

    amt_to_find = 4
    i = amt_to_find

    for number in range(5, how_many_primes):
        num_primes = number_unique_prime_factors(number, primes)
        # print(f"{number}, {num_primes}")

        if (num_primes == amt_to_find):
            i -= 1
        else:
            i = amt_to_find

        if i == 0:
            return number - amt_to_find + 1


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
