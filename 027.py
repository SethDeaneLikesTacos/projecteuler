import pef
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

number = 1000

def main():
    maxn = 0
    maxtotal = 0
    total = 1
    primes = pef.prime_sieve(number * number)

    for b in range(number+1):
        for a in range(number+1):
            for n in range(number+1):
                sola = n**2 + a*n + b
                solb = n**2 - a*n + b
                solc = n**2 + a*n - b
                sold = n**2 - a*n - b
                print(str(n) + "^2 + " + str(a) + "*" + str(n) + " + " + str(b) + " = " + str(sola))

                if n > maxn:
                    print(a,b)
                    total = a * b
                    maxn = n

                if sol not in primes:
                    break


            if total > maxtotal:
                maxtotal = total
    pef.answer(maxtotal)

main()
