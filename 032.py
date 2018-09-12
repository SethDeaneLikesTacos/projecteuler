import pef
import time
"""
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The product 7254 is unusual, as the identity,
39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplie
/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one
way so be sure to only include it once in your sum.
"""

# a = multplicand
# b = multiplier
# c = product
def ispan(a, b, c):

    # create list of numbers from a, b, and c that
    # we want to check for pandigitality
    labc = list(str(a)) + list(str(b)) + list(str(c))
    ispan = list(map(int, labc))

    # initialize a know pandigital array for 1-9
    pan = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    # remove numbers from our know pandigital array
    for i in range(len(ispan)):
        if ispan[i] in pan:
            pan.remove(ispan[i])

    # if there are any numbers left in our know pandigital
    # array, then it a, b, and c are not pandigital
    if len(pan) == 0:
        return True
    else:
        return False


def main():
    start_time = time.time()

    # keep tally of the sum of pandigital products
    total = 0

    # check through any possible product
    for product in range(1, 9999):

        # find the two multipliers of that product
        for i in range(1, int(product/2)):
            if product % i == 0:
                a = i
                b = int(product / a)

                # make sure they are the right length to be 1-9 pandigital
                # then check if that compination is 1-9 pandigital
                if len(str(a)) + len(str(b)) + len(str(product)) == 9 and\
                        ispan(a, b, product):

                    # at this point we know that the combination is 1-9 pandigital
                    # and we can print the number and add the sum
                    # print(str(a) + " * " + str(b) + " = " + str(product) +\
                    # " and is pandigital")
                    
                    total += product
                    break

    end_time = time.time()
    pef.answer(total, end_time - start_time)

main()
