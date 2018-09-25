import resources.pef as pef
import time
"""
https://projecteuler.net/problem=11
"""


def main():

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
    
    return s


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
