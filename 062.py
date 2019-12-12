import resources.pef as pef
import time
"""
https://projecteuler.net/problem=62
1.1786422729492188
"""


def main():

    lst_orig = []
    lst_sort = []
    lst_occr = []

    for i in range(100000):
        i3 = i ** 3
        i3_srt = ''.join(sorted(str(i3)))

        if i3_srt in lst_sort:
            indx = lst_sort.index(i3_srt)
            lst_occr[indx] += 1

            if 5 in lst_occr:
                return lst_orig[indx]

        else:
            lst_orig.append(i3)
            lst_sort.append(i3_srt)
            lst_occr.append(1)


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)   
