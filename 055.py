import resources.pef as pef
import time
"""
https://projecteuler.net/problem=55
"""


def main():

    total = 0
    for i in range(10000):
        reverse_appended = int(str(i)) + int(str(i)[::-1])

        for j in range(50):

            # if palindromatic
            if str(reverse_appended) ==  str(reverse_appended)[::-1]:
                break

            if j == 49:
                total += 1

            reverse_appended = int(str(reverse_appended)) + int(str(reverse_appended)[::-1])

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
