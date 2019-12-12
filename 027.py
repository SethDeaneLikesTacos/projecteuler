import resources.pef as pef
import time
"""
https://projecteuler.net/problem=27
8.877437829971313
"""


def main():

    maxn = 0
    answer = 0
    for a in range(-1000,1001):
        for b in range(-1000,1000):
            streak = 0
            for n in range(80):

                if pef.is_prime(n**2 + (n*a) + b):
                    streak += 1
                else:
                    break

                if maxn <= n:
                    maxn = n
                    answer = a * b

    return answer


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
