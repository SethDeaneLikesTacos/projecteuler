import resources.pef as pef
import time
"""
https://projecteuler.net/problem=13
0.0005609989166259766
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
