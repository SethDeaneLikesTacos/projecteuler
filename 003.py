import resources.pef as pef
import time
import math
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def main():

    number = 600851475143
    for i in range(int(math.sqrt(number)), 1, -1):
        if pef.isprime(i) and number % i == 0:

        	return i


if __name__ == "__main__":
	start_time = time.time()
	answer = main()
	end_time = time.time()
	pef.answer(answer, end_time - start_time)