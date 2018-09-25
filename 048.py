import resources.pef as pef
import time
"""
https://projecteuler.net/problem=48
"""


def main():
    total = 0
    for i in range(1,1001):
        total += i**i
    return str(total)[-10:]


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
