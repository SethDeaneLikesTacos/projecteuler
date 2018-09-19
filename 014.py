import resources.pef as pef
import time
"""
The following iterative sequence is defined for the set of positive integers:

     n → n/2 (n is even)
     n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def main():

    maxlen = 0

    for i in range(1000000, 1, -1):
        n = i
        l = 1

        while n > 1:
            l += 1
            if n % 2 == 0:
                n /= 2
            elif n % 2 == 1:
                n = 3 * n + 1

        if l > maxlen:
            maxlen = l
            maxstart = i

    return maxstart


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)