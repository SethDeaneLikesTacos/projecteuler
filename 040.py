import resources.pef as pef
import time
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


def main():

    # generate number
    num_str = ''
    for i in range(1, 1000009):
        num_str += str(i)

    # find the value by multiplying the value at the indexes of "number"
    total = 1
    numbers = [0, 9, 99, 999, 9999, 99999, 999999]
    for i in numbers:
        total *= int(num_str[i])

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
