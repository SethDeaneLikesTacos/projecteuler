import resources.pef as pef
import time
"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes
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
            if pef.isprime(int(str(i)[d::])) and pef.isprime(int(str(i)[0:d+1])):
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
