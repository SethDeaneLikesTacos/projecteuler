import resources.pef as pef
import time
"""
https://projecteuler.net/problem=67
0.00482487678527832
"""


dim = 100

def main():

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

    return pyramid[0][0]


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
