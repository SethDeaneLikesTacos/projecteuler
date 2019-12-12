import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=20
0.00007081031799316406
"""


n = 100
def main():
    start_time = time.time()

    b = math.factorial(n)

    return sum([int(i) for i in str(b)])


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
