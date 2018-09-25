import resources.pef as pef
import time
"""
https://projecteuler.net/problem=22
"""


def main():

    total = 0
    names = open("resources/022.txt", "r").read().replace('"', "").split(',')
    names.sort()
    
    for name in names:
        i = names.index(name) + 1

        namesum = 0
        for letter in name:
            namesum += ord(letter) - 64
        namesum = namesum * i
        total += namesum

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
