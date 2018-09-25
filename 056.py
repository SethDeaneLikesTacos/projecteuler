import resources.pef as pef
import time
"""
https://projecteuler.net/problem=56
"""


def main():
    num = 100
    max_digital_sum = 0
    for a in range(num):
        for b in range(num):
            a_tothe_b = a**b
            digital_sum = sum(map(int, str(a_tothe_b)))
            # print(f"{digital_sum}, {a_tothe_b}")
            if digital_sum > max_digital_sum:
                max_digital_sum = digital_sum

    return max_digital_sum


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
