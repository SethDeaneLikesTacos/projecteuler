import resources.pef as pef
import time
"""
https://projecteuler.net/problem=39
"""


def main():

    minimum = 1
    maximum = 1000

    d = {}
    for i in range(minimum, maximum+1):
        d[i] = 0

    for a in range(1, maximum//2):
        for b in range(a, maximum//2):
            for c in range(b, maximum//2):

                if a*a + b*b == c*c and minimum <= a+b+c <= maximum:
                    # print(str(a) + " " + str(b) + " " + str(c) + " is a right triangle")
                    d[a+b+c] += 1

    maximized = max(d, key=d.get)

    return maximized


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
