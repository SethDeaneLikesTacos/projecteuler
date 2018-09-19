import resources.pef as pef
import time
"""
The four adjacent digits in the 1000-digit number that have
the greatest product are 9 × 9 × 8 × 9 = 5832.

   73167176531330624919225119674426574742355349194934
   ... (Matrix can be found in resources/008.txt) ...
   71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number
that have the greatest product. What is the value of this product?
"""


def main():

    # read from file to array
    ar = []
    raw_list = open("resources/008.txt", "r").read().replace('\n', '')
    for i in raw_list:
        ar.append(int(i))

    arraylen = 1000
    digits = 13
    maxprod = 0
    for i in range(arraylen - digits + 1):
        prod = 1
        for j in range(digits):
            prod *= ar[i+j]
        if prod > maxprod:
            maxprod = prod

    return maxprod


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
