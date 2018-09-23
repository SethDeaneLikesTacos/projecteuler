import resources.pef as pef
import time
from itertools import permutations

def degree_prime_family(number, unidentifieds):


    ar = [] # define the array that will hold the various number we are looking through
    max_num_primes = 0  # define the variables for the max num of primes
    smallest_prime = 9999999  # define the smallest prime number that is looked for in return

    # turn the number in to an array
    for i in str(number):
        ar.append(str(i))

    # add in the declared number of unknown asterics
    for i in range(unidentifieds):
        ar.append('*')

    # loop through each permutation
    for perm in list(permutations(ar)):

        # the empty permutation with and *'s'
        perm_empty = ''.join(perm)

        num_primes = 0      # count the number of primes for that permutation
        first_prime = 0     # keep track of the first prime for a permutation
        found_prime = False # check if we have found the first prime
        for j in range(10):

            # the completed permutation without and *'s'
            perm_filled = perm_empty.replace("*",str(j))

            # if the number begins with 0, we want to ignore it
            if perm_filled[0] == "0":
                continue

            # keep track of the first prime found in the permutation
            if pef.isprime(int(perm_filled)) and found_prime == False:
                first_prime = int(perm_filled)
                found_prime = True

            if pef.isprime(int(perm_filled)):
                num_primes += 1

                if num_primes >= max_num_primes:
                    smallest_prime = first_prime

            if max_num_primes < num_primes:
                max_num_primes = num_primes

    return max_num_primes, smallest_prime


def main():

    for i in range(10, 10000):
        for j in range(1,4):
            max_p, smol_prime = degree_prime_family(i, j)

            if max_p == 8:
                return smol_prime


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
