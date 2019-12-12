import resources.pef as pef
import time
"""
https://projecteuler.net/problem=7
0.20600104331970215
"""


def main():

    i = 1
    count = 1
    while count < 10001:
        i += 1
        if pef.is_prime(i):
            count += 1

    return i


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
