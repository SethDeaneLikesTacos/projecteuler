import resources.pef as pef
import time
"""
https://projecteuler.net/problem=42
"""


def main():

    words = open("resources/042.txt", "r").read().replace('"', "").split(',')
    num_triangle = 0

    # list of triangle numbers
    tns = []
    for i in range(1, 500):
        tns.append(int((1/2) * i * (i+1)))

    for word in words:
        word_val = 0
        for letter in word:
            let_val = ord(letter) - 64
            # print(letter + " " + str(let_val))
            word_val += let_val

        # check if word val is a triangle number
        if word_val in tns:
            num_triangle += 1
        # print(word + " " + str(word_val))

    return num_triangle


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
