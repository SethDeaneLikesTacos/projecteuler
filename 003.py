import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=3
"""


def main():

    number = 600851475143
    for i in range(int(math.sqrt(number)), 1, -1):
        if pef.is_prime(i) and number % i == 0:

        	return i


if __name__ == "__main__":
	start_time = time.time()
	answer = main()
	end_time = time.time()
	pef.answer(answer, end_time - start_time)
