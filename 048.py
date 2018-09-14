import pef
import time
"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


def main():
    total = 0
    for i in range(1,1001):
        total += i**i
    return str(total)[-10:]
    # 9110846700


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
