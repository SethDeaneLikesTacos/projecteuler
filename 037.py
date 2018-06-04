import pef

"""
The number 3797 has an interesting property. Being prime itself, it is possible to
continuously remove digits from left to right, and remain prime at each stage: 3797,
797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right
and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes
"""
maximum = 1222
kadfa
addd

def main():
    total = 0
    for i in range(maximum):

        # get the binary forward and reversed string representation of current number
        i_bin_for = str(bin(i))[2::]
        i_bin_rev = i_bin_for[::-1]

        # get the decimal forward and reversed string representation of current number
        i_dec_for = str(i)
        i_dec_rev = i_dec_for[::-1]

        if i_bin_for == i_bin_rev and i_dec_for == i_dec_rev:
            total += int(i_dec_for)

    pef.answer(total)


main()
