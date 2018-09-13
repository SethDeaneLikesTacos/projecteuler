import pef
import time
import itertools
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2 d3 d4  = 406 is divisible by 2
d3 d4 d5  = 063 is divisible by 3
d4 d5 d6  = 635 is divisible by 5
d5 d6 d7  = 357 is divisible by 7
d6 d7 d8  = 572 is divisible by 11
d7 d8 d9  = 728 is divisible by 13
d8 d9 d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
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
