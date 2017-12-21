import pef
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage.
"""

total = 0

def identify_ones(n):
    global total
    if n == 1 or n == 2 or n == 6:
        total += 3
    if n == 4 or n == 5 or n == 9:
        total += 4
    if n == 3 or n == 7 or n == 8:
        total += 5


def identify_teens(n):
    global total
    if n == 10:
        total += 3
    if n == 11 or n == 12:
        total += 6
    if n == 15:
        total += 7
    if n == 13 or n == 14:
        total += 8
 

def identify_tens(n):
    global total
    if n == 1:
        total += 4
    if n == 4 or n == 5 or n == 6:
        total += 5
    if n == 2 or n == 3 or n == 8 or n == 9:
        total += 6
    if n == 7:
        total += 7


def main():
    global total
    lasttotal = 0

    for i in range(1, 1001):

        one = (i % 10) // 1
        ten = (i % 100) // 10
        teen = (ten * 10) + one
        hun = (i % 1000) // 100

        # 1000
        if i == 1000:
            total += 11

        # hundreds place taking and into account
        if hun != 0 and ten == 0 and one == 0:
            identify_ones(hun)
            total += 7
        if hun != 0 and (ten != 0 or one != 0):
            identify_ones(hun)
            total += 10
        
        # 10-15, above 15, 18 is a weird case
        if 10 <= teen and teen <= 15:
            identify_teens(teen)
        if teen > 15 and teen != 18:
            identify_tens(ten)
            identify_ones(one)

        if teen == 18:
            total += 8

        # ones place
        if ten == 0:
            identify_ones(one)

        lasttotal = total;

    pef.answer(total)

main()

