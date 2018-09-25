import resources.pef as pef
import time
import itertools
"""
https://projecteuler.net/problem=43
"""


def intlist_to_int(intlist):
    returnable = ''
    for i in intlist:
        returnable += (str(i))
    return int(returnable)


def main():

    h = list(itertools.permutations([1,2,3,4,5,6,7,8,9,0]))
    total = 0

    for i in h:
        one = intlist_to_int([i[1], i[2], i[3]])
        two = intlist_to_int([i[2], i[3], i[4]])
        three = intlist_to_int([i[3], i[4], i[5]])
        four = intlist_to_int([i[4], i[5], i[6]])
        five = intlist_to_int([i[5], i[6], i[7]])
        six = intlist_to_int([i[6], i[7], i[8]])
        seven = intlist_to_int([i[7], i[8], i[9]])

        if len(i) == 10 and \
            one % 2 == 0 and \
            two % 3 == 0 and \
            three % 5 == 0 and \
            four % 7 == 0 and \
            five % 11 == 0 and \
            six % 13 == 0 and \
            seven % 17 == 0:
            # print(intlist_to_int([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]))
            total += intlist_to_int([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
