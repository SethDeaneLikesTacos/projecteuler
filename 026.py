import pef
import decimal
import re
"""
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators 2 to 10 are given:

1/2   =   0.5
1/3   =   0.(3)
1/4   =   0.25
1/5   =   0.2
1/6   =   0.1(6)
1/7   =   0.(142857)
1/8   =   0.125
1/9   =   0.(1)
1/10  =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""
maxdecs = 9999
d = 1001

def cyclelen(n):
    cl = 0  # cycle length
    regex = re.compile(r"([0-9]+?)\1+")
    match = regex.search(str(n))
    if match != None:
        cl = len(match.group(1))
    return cl


def main():
    # define how many decimal places there are
    decimal.getcontext().prec = maxdecs
    maxd = 0
    count = 1
    maxrecur = 0

    for i in range(2, d):
        count += 1
        div = 1 / decimal.Decimal(i)

        # get the decimal portion of the number
        dec = int(str(div).split('.')[1])
        cl = cyclelen(dec)

        # keep track of max
        if cl > maxrecur:
            maxrecur = cl
            maxd = count

    pef.answer(maxd)

main()
