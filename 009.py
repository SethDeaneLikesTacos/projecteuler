import resources.pef as pef
import time
"""
https://projecteuler.net/problem=9
0.16497373580932617
"""


def main():

    maximum = 1000

    for a in range(1, int(maximum/2)):
        for b in range(1, int(maximum/2)):
            c = (a**2 + b**2)**.5
            hyp = a**2 + b**2
            if a+b+c == maximum and hyp**.5 == c and a<b and b<c:

                return int(a*b*c)


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
