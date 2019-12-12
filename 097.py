import resources.pef as pef
import time
"""
https://projecteuler.net/problem=97
83.98430299758911
"""


def main():
    return str((28433*(2**7830457))+1)[-10:]


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
