import resources.pef as pef
import time
"""
https://projecteuler.net/problem=40
0.4363381862640381
"""


def main():

    # generate number
    num_str = ''
    for i in range(1, 1000009):
        num_str += str(i)

    # find the value by multiplying the value at the indexes of "number"
    total = 1
    numbers = [0, 9, 99, 999, 9999, 99999, 999999]
    for i in numbers:
        total *= int(num_str[i])

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
