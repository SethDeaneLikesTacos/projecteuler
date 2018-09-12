import pef
import time
import math
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

n = 100
def main():
    start_time = time.time()

    b = math.factorial(n)

    end_time = time.time()
    pef.answer(sum([int(i) for i in str(b)]), end_time - start_time)

main()
