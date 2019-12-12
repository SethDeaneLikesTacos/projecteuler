import resources.pef as pef
import time
"""
https://projecteuler.net/problem=6
0.00008320808410644531
"""


def main():

    maximum = 100
    sq = 0
    sumsq = 0
    for i in range(1, maximum+1):
        sq += i ** 2
        sumsq += i

    sumsq = sumsq ** 2

    return sumsq - sq
    

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
