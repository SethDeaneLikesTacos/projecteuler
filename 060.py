import resources.pef as pef
import time
import math
from itertools import combinations, permutations
"""
https://projecteuler.net/problem=60

"""


def main():

    primes = pef.prime_sieve(700)
    group_size = 4
    prime_groups = combinations(primes, group_size) 

    
    for prime_group in list(prime_groups):
        prime_pairs = permutations(prime_group, 2)

        count = 0

        for prime_pair in list(prime_pairs):
            concat_prime_pair = int(str(prime_pair[0]) + str(prime_pair[1]))

            if pef.is_prime(concat_prime_pair):
                count += 1

            if count == math.factorial(group_size):
                total = 0
                for i in range(group_size):
                    total += prime_group[i]
                return total

        
    return "faksjh"


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
