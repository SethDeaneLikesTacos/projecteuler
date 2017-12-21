import pef
"""
A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be
shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
"""

maximum = 28123

def genabnums(maximum):
    abnums = set()
    for i in range(10, maximum):
        facs = []
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                facs.append(j)
        if sum(facs) > i:
            abnums.add(i)
    
    return abnums


def main():
    sumtot = 0
    ovetot = 0
    abnums = genabnums(maximum)

    for i in range(maximum):
        ovetot += i
        for a in abnums:
            if i - a in abnums:
                sumtot += i
                break

    pef.answer(ovetot - sumtot)
        


main()


