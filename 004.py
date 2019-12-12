import resources.pef as pef
import time
"""
https://projecteuler.net/problem=4
1.3023569583892822
"""


def main():

    maxpal = 0
    for i in range(1000, 1, -1):
        for j in range(1000, 1, -1):
            product = i * j
            revproduct = pef.reverse_num(product)
            if revproduct == product and product > maxpal:
                maxpal = product

    return maxpal


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
