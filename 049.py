import pef
import time
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

NOTE: This one takes about 40 seconds
"""


def main():

    # generate primes from 1000 - 9999
    primes = pef.prime_sieve(9999)[168:]

    for i in primes:
        for j in primes:
            if j < i: continue
            for k in primes:
                if k < j: continue
                if abs(i - j) == abs(j - k) and \
                    i != j and i != k and j != k and \
                    sorted(map(int, str(i))) == sorted(map(int, str(j))) and \
                    sorted(map(int, str(j))) == sorted(map(int, str(k))) and \
                    i != 1487:

                    return ''.join(str(i) + str(j) + str(k))


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
