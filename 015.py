import resources.pef as pef
import time
"""
https://projecteuler.net/problem=15
0.0
SOLUTION: 40! / (20! * 20!) = 137846528820
"""


def main():

    return 137846528820


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
