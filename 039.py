import resources.pef as pef
import time
"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
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
