import resources.pef as pef
import time
import decimal
import re
"""
https://projecteuler.net/problem=26
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

    return maxd


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
