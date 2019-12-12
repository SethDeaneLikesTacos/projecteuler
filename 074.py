import resources.pef as pef
import time
import math
"""
https://projecteuler.net/problem=74
96.12918090820312
"""

def main():
    total = 0
    maximum = 1000000
    chain_length = 60
    for starting_number in range(1,maximum):

        # declare variables
        chain = 0
        current_number = starting_number
        previous_numbers = [starting_number]

        for i in range(chain_length+1):

            # compute the summed factorial of each digit
            fact_sum = 0
            for digit in str(current_number):
                fact_sum += math.factorial(int(digit))

            # update the current number
            current_number = fact_sum

            if chain == chain_length-1 and current_number in previous_numbers:
                total += 1
                break

            if current_number in previous_numbers:
                break

            chain += 1
            previous_numbers.append(current_number)
    return total

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)