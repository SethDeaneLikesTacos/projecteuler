import resources.pef as pef
import time
"""
https://projecteuler.net/problem=8
0.0026040077209472656
"""


def main():

    # read from file to array
    ar = []
    raw_list = open("resources/008.txt", "r").read().replace('\n', '')
    for i in raw_list:
        ar.append(int(i))

    arraylen = 1000
    digits = 13
    maxprod = 0
    for i in range(arraylen - digits + 1):
        prod = 1
        for j in range(digits):
            prod *= ar[i+j]
        if prod > maxprod:
            maxprod = prod

    return maxprod


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
