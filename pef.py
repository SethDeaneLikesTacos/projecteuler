import math

def is_pandigital_19(number):
    """
    checks for pandigitality (if there is one of each digit "1-9" in the number)
    :param number: number we are checking pandigitality
    :return: True if pandigital
    """
    checked = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1, 10):
        if str(i) in str(number):
            checked[i-1] = 0
    if len(str(number)) == 9 and len(set(checked))==1:
        return True
    else:
        return False


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


def prime_sieve(minimum, maximum):
    """
    Efficiently creates a set with all prime numbers
    below the input maximum.
    WARNING: maximum over 9999999 is bad news
    """
    limitn = maximum + 1
    not_prime = set()
    primes = set()
    for i in range(minimum, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.add(i)
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

def answer(number):
    print("ANSWER: " + str(number))
