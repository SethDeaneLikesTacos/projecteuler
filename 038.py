import pef

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def main():
    maximum = 0

    # initial number
    for i in range(1, 10000):
        num_str = ""

        # list to multiply against
        for j in range(1, 100):
            num_int = i * j
            num_str += str(num_int)

            # we only want to check pandigitality if its a 9 digit number
            if len(num_str) == 9:

                if int(num_str) > maximum and pef.is_pandigital(int(num_str), len(num_str)):
                    maximum = int(num_str)

    pef.answer(maximum)


main()
