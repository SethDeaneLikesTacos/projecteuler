import resources.pef as pef
import time
"""
https://projecteuler.net/problem=1
0.00013589859008789062
"""


def main():

    maximum = 1000
    total = 0

    for i in range(maximum):
        if i % 3 == 0 or i % 5 == 0:
            total += i;

    return total


if __name__ == "__main__":
	start_time = time.time()
	answer = main()
	end_time = time.time()
	pef.answer(answer, end_time - start_time)
