import resources.pef as pef
import time
"""
https://projecteuler.net/problem=57
0.003215789794921875
"""


def main():
    numerator = 3
    denominator = 2
    total = 0
    
    for i in range(1000):
        if len(str(numerator)) > len(str(denominator)):
            total += 1

        temp = denominator
        denominator += numerator
        numerator += temp * 2

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
