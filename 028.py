import pef
import math
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

dim = 1001

def main():
    total = 1   # total sum thus far
    count = 1   # current number along the diagonal
    diff = 2    # the length difference between corners of the box

    for i in range( math.floor(dim/2) * 4):
        
        count += diff
        if i % 4 == 3:
            diff += 2
        total += count

    pef.answer(total)


main()
    
