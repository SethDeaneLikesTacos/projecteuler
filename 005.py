import pef
"""
2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
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

    pef.answer(smallestdiv)


main()
