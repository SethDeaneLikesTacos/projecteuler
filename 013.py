import pef
import time
"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    7432...
"""


def main():

    # read array from file to array
    array = []
    raw_list = open("resources/013.txt", "r").read().split('\n')
    for i in raw_list:
        if len(i) >= 3:
            array.append(int(i))

    x = 0
    for i in range(len(array)):
        x = x + array[i]

    return str(x)[:10]


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
