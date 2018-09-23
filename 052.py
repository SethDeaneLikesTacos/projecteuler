import resources.pef as pef
import time
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""
def main():

	for i in range(1,1000000):
		multiplication_array = []

		for j in range(1,7):
			product = i*j
			sorted_product = ''.join(sorted(str(product)))
			multiplication_array.append(int(sorted_product))

		if multiplication_array[1:] == multiplication_array[:-1]:
			return i


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
