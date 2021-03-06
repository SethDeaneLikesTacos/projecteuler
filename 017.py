import resources.pef as pef
import time
"""
https://projecteuler.net/problem=17
0.0017430782318115234
"""


total = 0

def identify_ones(n):
    global total
    if n == 1 or n == 2 or n == 6:
        total += 3
    if n == 4 or n == 5 or n == 9:
        total += 4
    if n == 3 or n == 7 or n == 8:
        total += 5


def identify_teens(n):
    global total
    if n == 10:
        total += 3
    if n == 11 or n == 12:
        total += 6
    if n == 15:
        total += 7
    if n == 13 or n == 14:
        total += 8


def identify_tens(n):
    global total
    if n == 1:
        total += 4
    if n == 4 or n == 5 or n == 6:
        total += 5
    if n == 2 or n == 3 or n == 8 or n == 9:
        total += 6
    if n == 7:
        total += 7


def main():

    global total

    for i in range(1, 1001):

        one = (i % 10) // 1
        ten = (i % 100) // 10
        teen = (ten * 10) + one
        hun = (i % 1000) // 100

        # 1000
        if i == 1000:
            total += 11

        # hundreds place taking and into account
        if hun != 0 and ten == 0 and one == 0:
            identify_ones(hun)
            total += 7
        if hun != 0 and (ten != 0 or one != 0):
            identify_ones(hun)
            total += 10

        # 10-15, above 15, 18 is a weird case
        if 10 <= teen and teen <= 15:
            identify_teens(teen)
        if teen > 15 and teen != 18:
            identify_tens(ten)
            identify_ones(one)

        if teen == 18:
            total += 8

        # ones place
        if ten == 0:
            identify_ones(one)

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
    
