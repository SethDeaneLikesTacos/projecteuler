import pef
import time
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
    start_time = time.time()

    maximum = 1000

    for a in range(1, int(maximum/2)):
        for b in range(1, int(maximum/2)):
            c = (a**2 + b**2)**.5
            hyp = a**2 + b**2
            if a+b+c == maximum and hyp**.5 == c and a<b and b<c:

                end_time = time.time()
                pef.answer(int(a*b*c), end_time - start_time)
                return

main()
