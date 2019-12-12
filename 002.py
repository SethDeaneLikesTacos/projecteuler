import resources.pef as pef
import time
"""
https://projecteuler.net/problem=2
0.000028848648071289062
"""


def main():

    total = 0
    maximum = 4000000
    fibnums = pef.gen_fib(maximum)

    for i in fibnums:
        if i%2 == 0:
            total += i
    
    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
