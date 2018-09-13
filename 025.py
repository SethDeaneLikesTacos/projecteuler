import pef
import time
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fib(fibl):
    tmp = fibl[0] + fibl[1]
    fibl[1] = fibl[0]
    fibl[0] = tmp
    return fibl


def main():

    fibl = [1,1]
    for i in range(3, 5000):
        fibl = fib(fibl)
        nDigits = len(str(fibl[0]))
        if nDigits == 1000:
            break

    return i


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
