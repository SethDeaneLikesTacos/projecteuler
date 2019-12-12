import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=179
"""

def main():
    maximum = 10 ** 7
    prev_count = 0
    total = 0

    for i in range(maximum):
        # print(f'-- {i} --')

        curr_count = 1
        for j in range(1,math.ceil(math.sqrt(i))):
            if i % j == 0:
                curr_count += 1
                # print(j)

        if prev_count == curr_count:
            total += 1

        prev_count = curr_count
        
    print(total)


    
    return pef.is_prime(4)

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)