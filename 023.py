import resources.pef as pef
import time
"""
https://projecteuler.net/problem=23
18.82033109664917
"""


maximum = 28123

def genabnums(maximum):
    abnums = set()
    for i in range(10, maximum):
        facs = []
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                facs.append(j)
        if sum(facs) > i:
            abnums.add(i)

    return abnums


def main():

    sumtot = 0
    ovetot = 0
    abnums = genabnums(maximum)

    for i in range(maximum):
        ovetot += i
        for a in abnums:
            if i - a in abnums:
                sumtot += i
                break

    return ovetot - sumtot


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
