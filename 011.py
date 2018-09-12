import pef
import time
"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

 8  2 22 97 38 15 00 40 00 75  4  5  7 78 52 12 50 77 91 08
    ... (Matrix can be found in resources/011.txt) ...
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""


def main():
    start_time = time.time()

    # read file array from file
    array = []
    raw_list = open("resources/011.txt", "r").read().split('\n')
    for i in raw_list:
        ar = i.split(" ")
        array.append(ar)

    # convert the strs to ints
    for i in range(0,20):
        for j in range(0,20):
            array[i][j] = int(array[i][j])

    dim = 20
    l = 4
    s = 0

    for i in range(dim):
        for j in range(dim):

            # Vertical check
            if i + l <= dim:
                vsum = array[i][j] * array[i+1][j] * array[i+2][j] * array[i+3][j]
                if s < vsum:
                    s = vsum

            # Horizontal check
            if j + l <= dim:
                hsum = array[i][j] * array[i][j+1] * array[i][j+2] * array[i][j+3];
                if s < hsum:
                    s = hsum

            # Down right check
            if i + l <= dim and j + l <= dim:
                dsum_right = array[i][j] * array[i+1][j+1] * array[i+2][j+2] * array[i+3][j+3]
                if s < dsum_right:
                    s = dsum_right

            # Down left check
            if i + l <= dim and j - l > 0:
                dsum_left = array[i][j] * array[i+1][j-1] * array[i+2][j-2] * array[i+3][j-3]
                if s < dsum_left:
                    s = dsum_left

    end_time = time.time()
    pef.answer(s, end_time - start_time)

main()
