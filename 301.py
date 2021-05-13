import resources.pef as pef
import time
"""
https://projecteuler.net/problem=301

NOTE: Takes a hot minute
"""

maxnum = 2 ** 30 +1

def main():

    count = 0

    for i in range(1, maxnum):
        
        # setup 3 heaps
        A = i
        B = 2*i
        C = 3*i

        nimsum = A ^ B ^ C

        if nimsum == 0:
            count += 1

    return count

if __name__ == "__main__":
    print(maxnum)
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)


