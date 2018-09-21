import resources.pef as pef
import time
"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 ≤ n ≤ 39. However, when n=40, 40^2 + 40 + 41 = 40
(40+1) + 41 is divisible by 41, and certainly when n=41,41^2 + 41 + 41
is clearly divisible by 41.

The incredible formula n2−79n+1601n2−79n+1601 was discovered, which
produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product
of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of nn
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, aa and bb, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""


def main():

    maxn = 0
    answer = 0
    for a in range(-1000,1001):
        for b in range(-1000,1000):
            streak = 0
            for n in range(80):

                if pef.isprime(n**2 + (n*a) + b):
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
