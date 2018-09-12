import pef
import time
"""
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

     3
    7 4
   2 4 6
  8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)
"""

dim = 100

def main():
    start_time = time.time()

    # read array from file to array
    pyramid = []
    raw_list = open("resources/067.txt", "r").read().split('\n')
    for i in raw_list:
        ar = i.split(" ")
        pyramid.append(ar)

    # convert the strs to ints
    for i in range(0,dim):
        for j in range(len(pyramid[i])):
            pyramid[i][j] = int(pyramid[i][j])

    for i in range(dim-1, 0, -1):
        for j in range(0, dim - 1):

            if j > i-1:
                break

            if pyramid[i][j] > pyramid[i][j+1]:
                pyramid[i-1][j] += pyramid[i][j]

            elif pyramid[i][j] <= pyramid[i][j+1]:
                pyramid[i-1][j] += pyramid[i][j+1]

    end_time = time.time()
    pef.answer(pyramid[0][0], end_time - start_time)

main()
