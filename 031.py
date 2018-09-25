import resources.pef as pef
import time
"""
https://projecteuler.net/problem=31
"""


coins = [200, 100, 50, 20, 10, 5, 2, 1]
value = 200

def main():

    count = 0
    for a in range(int(value/coins[0]) + 1):
        for b in range(int(value/coins[1]) + 1):
            if a*coins[0] + b*coins[1] > value:
                continue
            for c in range(int(value/coins[2]) + 1):
                if a*coins[0] + b*coins[1] + c*coins[2] > value:
                    continue
                for d in range(int(value/coins[3]) + 1):
                    if a*coins[0] + b*coins[1] + c*coins[2] + d*coins[3] > value:
                        continue
                    for e in range(int(value/coins[4]) + 1):
                        if a*coins[0] + b*coins[1] + c*coins[2] + d*coins[3] + e*coins[4] > value:
                            continue
                        for f in range(int(value/coins[5]) + 1):
                            if a*coins[0] + b*coins[1] + c*coins[2] + d*coins[3] + e*coins[4] + f*coins[5] > value:
                                continue
                            for g in range(int(value/coins[6]) + 1):
                                if a*coins[0] + b*coins[1] + c*coins[2] + d*coins[3] + e*coins[4] + f*coins[5] + g*coins[6] > value:
                                    continue
                                for h in range(int(value/coins[7]) + 1):
                                    if a*coins[0] + b*coins[1] + c*coins[2] + d*coins[3] + e*coins[4] + f*coins[5] + g*coins[6] + h*coins[7]> value:
                                        continue

                                    if a*coins[0] + b*coins[1] + c*coins[2] + d*coins[3] + e*coins[4] + f*coins[5] + g*coins[6] + h*coins[7] == value:
                                        count += 1

    return count


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
