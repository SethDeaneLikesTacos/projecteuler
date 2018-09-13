import pef
import time
"""
The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of
fraction, less than one in value, and containing two digits in
the numerator and denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""


def simplifyfraction(a, b):
    for i in range(b-1, 2, -1):
        if (a/i) / (b/i) == a/b and a/i % 1 == 0 and b/i % 1 == 0:
            return a/i, b/i
    else:
        return a, b


def main():

    total = 1

    for i in range(10, 100):
        for j in range(10, 100):

            li = [int(x) for x in str(i)]
            lj = [int(x) for x in str(j)]

            for k in li:
                if k in lj and \
                        i < j and \
                        (li[0] != li[1] and lj[0] != lj[1]) and \
                        (li[1] != 0 and lj[1] != 0):

                    li.remove(k)
                    lj.remove(k)
                    div1 = i / j
                    div2 = li[0] / lj[0]

                    if div2 == div1:
                        a, b = simplifyfraction(li[0], li[0])
                        total *= a/b

    return int(total * 100)


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
