import resources.pef as pef
import time
import math
from itertools import combinations, permutations
"""
https://projecteuler.net/problem=60

"""


def main():

    primes = pef.prime_sieve(50)
    group_size = 3
    prime_groups = combinations(primes, group_size)
    print(list(prime_groups))
    print(list(prime_groups)[1])

    print("Done making combinations...")
    
    for prime_group in list(prime_groups):

        # ignore 2 and 5, which would never create a possible solution
        if (2 in prime_group) or (5 in prime_group):
            continue

        prime_pairs = permutations(prime_group, 2)
        count = 0

        for prime_pair in list(prime_pairs):

            concat_prime_pair = int(str(prime_pair[0]) + str(prime_pair[1]))

            if pef.is_prime(concat_prime_pair):
                count += 1

        # 12 for group_size of 4 (4 pick 2 = 12)
        # 20 for group_size of 5 (5 pick 2 = 20)
        if count == 20:
            return sum(prime_group)

        # print("count: " + str(count))
        # print("sum: " + str(sum(prime_group)))
        # if sum(prime_group) == 792:
        #     break


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
