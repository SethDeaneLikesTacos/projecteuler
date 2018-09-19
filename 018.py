import resources.pef as pef
import time
"""
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

     3
    7 4
   2 4 6
  8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                    75
 ...                                    ...
 4 62 98 27 23  9 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method! ;o)
"""


dim = 15

def main():

    # read array from file to array
    pyramid = []
    raw_list = open("resources/018.txt", "r").read().split('\n')
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

    return pyramid[0][0]


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
    