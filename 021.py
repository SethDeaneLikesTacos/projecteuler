import resources.pef as pef
import time
"""
https://projecteuler.net/problem=21
"""


maximum = 10000

def main():

    total = 0

    for i in range(maximum):
        pair = 0
        pair2 = 0
        for j in range(i//2, 0, -1):
            if i % j == 0:
                pair += j

        for k in range(pair//2, 0, -1):
            if pair % k == 0:
                pair2 += k

        if i == pair2 and pair != pair2:
            total += i

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
