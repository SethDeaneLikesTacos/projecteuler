import resources.pef as pef
import time
"""
https://projecteuler.net/problem=5
"""


def main():

    currdiv = 0
    smallestdiv = 1

    for j in range(20):
        currdiv += 1
        count = 1
        maxi = smallestdiv

        while maxi % currdiv != 0:
            count = count + 1
            maxi = smallestdiv * count
        smallestdiv = maxi

    return smallestdiv


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
