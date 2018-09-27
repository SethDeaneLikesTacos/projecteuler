import resources.pef as pef
import time
"""
https://projecteuler.net/problem=59
"""


def main():
    encoded = open("resources/059.txt", "r").read().split(",")
    temp_encoded = open("resources/059.txt", "r").read().split(",")

    encoded = [int(i) for i in encoded]
    temp_encoded = [int(i) for i in temp_encoded]

    # generate all keys
    keys = []
    for i in range(97,123):
        for j in range(97,123):
            for k in range(97,123):
                key = []
                key.append(i)
                key.append(j)
                key.append(k)

                keys.append(key)

    # try decrypting with each key
    for k in keys:
        itt = 0
        for j in range(0, len(encoded)):
            temp_encoded[j] = encoded[j] ^ k[itt]
            if itt == 2:
                itt = 0
            else:
                itt += 1

        str_decoded = ''.join(chr(i) for i in temp_encoded)

        # if we think we found the correct key, stop
        if ("(The Gospel of John, chapter 1)" in str_decoded):
            return sum(bytearray(str_decoded, "ascii"))

    
if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
