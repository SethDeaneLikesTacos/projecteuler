import resources.pef as pef
import time
"""
https://projecteuler.net/problem=92
217.52900505065918
"""


def main():

    total = 0

    for i in range(1,10000000):

        number = i
        while True:

            if number == 89:
                total += 1
                break

            if number == 1:
                break

            # turn the starting number into a list of numbers
            tmp_list = [int(x) for x in str(number)]

            # sum the squares of the digits
            newNumber = sum([x**2 for x in tmp_list])

            # prepare next itteration
            number = newNumber

    return total

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
