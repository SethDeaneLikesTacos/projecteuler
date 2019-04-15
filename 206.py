import resources.pef as pef
import time
"""
https://projecteuler.net/problem=206

NOTE: Takes a hot minute
"""

def main():
    for p in range(1010101010, 1389026624):
        strp = str(p**2)

        if strp[0] != '1':
            continue
        if strp[2] != '2':
            continue
        if strp[4] != '3':
            continue
        if strp[6] != '4':
            continue
        if strp[8] != '5':
            continue
        if strp[10] != '6':
            continue
        if strp[12] != '7':
            continue
        if strp[14] != '8':
            continue
        if strp[16] != '9':
            continue
        if strp[18] != '0':
            continue

        return p

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)


