import resources.pef as pef
import time
"""
https://projecteuler.net/problem=37
"""


def main():

    total = 0
    num_found = 0

    primes = pef.prime_sieve(999999)

    for i in primes[4:]:
        count = 0

        # determine amount to remove from each end
        for d in range(len(str(i))):

            # check if the shortened numbers are prime
            if pef.is_prime(int(str(i)[d::])) and pef.is_prime(int(str(i)[0:d+1])):
                count += 1

        # if removing from both ends gave expected result
        if count == len(str(i)):
            # print(str(i) + " IS A TRUNCATABLE PRIME")
            num_found += 1
            total += i

        # a known stopping condition is when we find 11 such primes
        if num_found == 11:
            break

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
