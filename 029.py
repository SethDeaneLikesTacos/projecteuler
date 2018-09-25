import resources.pef as pef
import time
"""
https://projecteuler.net/problem=29
"""


def main():
    
    l = []

    for a in range(2, 101):
        for b in range(2, 101):
            x = a**b
            if x not in l:
                l.append(x)

    return len(l)


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
