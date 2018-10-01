import resources.pef as pef
import time
"""
https://projecteuler.net/problem=63
"""


def main():
    total = 0

    for i in range(1,10):
        for j in range(1,22):
            if len(str(i**j)) == j:
                # print(f"{i}^{j} = {i**j}")
                total += 1

    return total

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
