# Doing this one in python because
# the numbers will be super big

import math

n = 100
def main():
    b = math.factorial(n)
    print(sum([int(i) for i in str(b)]))

main()

