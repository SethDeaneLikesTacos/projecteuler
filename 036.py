import pef

"""
The number, 197, is called a circular prime because
all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7,
11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

maximum = 1000000
sum = 0



def main():
    for i in range(maximum):
        # get the binary forward and reversed string representation of current number
        i_bin_for = str(bin(i))
        i_bin_rev = reversed(i)

        # get the decimal forward and reversed string representation of current number
        i_dec_for = str(i)
        i_dec_rev = reversed(i)

        for k in range(len(i_bin_for) // 2):
            if i_bin_for[k] == i_bin_rev[k] and i_bin_for[k] == i_dec_rev[k]:
                sum +=


main()
