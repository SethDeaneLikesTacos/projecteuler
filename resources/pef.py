import math
import sys


def is_pandigital(nr, n):
    nr = str(nr)
    beg=nr[0:n]
    end=nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in beg or i not in end:
            return False
    return True


def isprime(n):
    """
    Returns True if n is prime
    Returns False if n is not prime
    """
    n = abs(int(n))
    if n == 2:
        return True
    if n < 2 or not n & 1:
        return False
    for i in range(3, int(n**.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_sieve(maximum):
    """
    Efficiently creates a set with all prime numbers
    below the input maximum.
    WARNING: maximum over 9999999 is bad news
    """
    limitn = maximum+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


def genfib(maximum):
    """
    Generates the list of fibonacci numbers below the maximum input
    Return: fibnums = list of fibonacci numbers
    """
    fibnums = [1]
    prev = 0
    curr = 1
    while curr <= maximum:
        tmep = curr + prev
        prev = curr
        curr = tmep
        if curr >= maximum:
            break
        fibnums.append(curr)
    return fibnums


def reversenum(number):
    reverse = 0
    while number > 0:
        reverse = (reverse * 10) + number % 10
        number = number // 10
    return reverse


def is_triangular(number):
    """
    Check if a number is triangular
    """
    maybe_triangular =  (math.sqrt(1 + 8 * number) - 1) / 2
    return maybe_triangular == int(maybe_triangular)


def is_pentagonal(number):
    """
    Check if a number is pentagonal
    """
    maybe_pentagonal =  (math.sqrt(1 + 24 * number) + 1) / 6
    return maybe_pentagonal == int(maybe_pentagonal)


def is_hexagonal(number):
    """
    Check if a number is hexagonal
    """
    maybe_hexagonal =  (math.sqrt(1 + 8 * number) + 1) / 4
    return maybe_hexagonal == int(maybe_hexagonal)


def answer(number, time_taken):
    current_file = sys.argv[0].split("/")[-1]    # get the running file name
    print(f"Answer to {current_file} is [{number}] and completed in [{time_taken}]")
