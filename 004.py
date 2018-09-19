import resources.pef as pef
import time
"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def main():

    maxpal = 0
    for i in range(1000, 1, -1):
        for j in range(1000, 1, -1):
            product = i * j
            revproduct = pef.reversenum(product)
            if revproduct == product and product > maxpal:
                maxpal = product

    return maxpal


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
