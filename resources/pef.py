import math
import sys


def is_pandigital(number):
    """
    Determine if a number is pandigital.
    https://en.wikipedia.org/wiki/Pandigital_number

    Args:
        number: Number to check for pandigitality.
    
    Returns:
        True if number is pandigital, False otherwise
    """
    number = str(number)
    len_number = len(number)
    beg = number[0:len_number]
    end = number[-len_number:]
    for i in map(str, range(1, len_number + 1)):
        if i not in beg or i not in end:
            return False
    return True


def is_prime(number):
    """
    Determines if a number is prime.

    Args:
        number: Number to evaluate for prime.
        
    Returns:
        True if number is prime, False otherwise.
    """
    # ensure that we are working with a positive int
    number = abs(int(number))

    # edge case for 2 since it is prime
    if number == 2:
        return True

    # not totally sure, but it works
    if number < 2 or not number & 1:
        return False

    # use modulous to check for prime
    for i in range(3, int(number**.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def prime_sieve(maximum):
    """
    Efficiently creates a set with all prime numbers below the input maximum.

    Args:
        maximum: Number to generate primes below.

    Returns:
        List containing all primes below the maximum number.
    """
    limitn = maximum+1
    not_prime = set()
    primes = []

    # check to make sure that we are within a usuable range
    if maximum <= 99999999:

        # calculate primes and add them to a list
        for i in range(2, limitn):
            if i in not_prime:
                continue

            for f in range(i*2, limitn, i):
                not_prime.add(f)

            primes.append(i)

    else:
        print("WARNING: The prime_sieve maximum you chose is dangerously high! (Primes not generated)")

    return primes


def gen_fib(maximum):
    """
    Generates the list of fibonacci numbers below the maximum input

    Args:
        maximum: Number to generate fibonacci sequence below.

    Returns:
        List of fibonacci numbers below the maximum.
    """
    fibnums = [1]
    prev = 0
    curr = 1
    while curr <= maximum:
        temp = curr + prev
        prev = curr
        curr = temp
        if curr >= maximum:
            break
        fibnums.append(curr)
    return fibnums


def reverse_num(number):
    """
    Reverse a number.
    E.g. 12345 = 54321

    Args:
        number: Number of forward number.

    Returns:
        Number in reverse.
    """
    reverse = 0
    while number > 0:
        reverse = (reverse * 10) + number % 10
        number = number // 10
    return reverse


def is_shape(number, shapeNumber):
    """
    Test if a number is of a "certain shape".
    Currently only setup for Triangular, Pentagonal, and Hexagonal.

    Args:
        number: number to test for a "certain shape".
        shapeNumber: number representing the "certain shape" to test.
            E.g. 3 for triangular, 6 for hexagonal

    Returns:
        True if number is of that shape, False otherwise.
    """

    # Test for triangular number (https://en.wikipedia.org/wiki/Triangular_number)
    if shapeNumber == 3:
        potentialNumber =  (math.sqrt(1 + 8 * number) - 1) / 2
    
    # Test for pentagonal number
    if shapeNumber == 5:
        potentialNumber =  (math.sqrt(1 + 24 * number) + 1) / 6

    # Test for hexagonal number (https://en.wikipedia.org/wiki/Hexagonal_number)
    if shapeNumber == 6:
        potentialNumber =  (math.sqrt(1 + 8 * number) + 1) / 4

    return potentialNumber == int(potentialNumber)


def answer(answer, time_taken):
    """
    Function that neatly formats the answer printing process.

    Args:
        answer: Answer to the question.
        time_taken: Time taken to solve the question.

    Returns:
        None, just prints the answer nicely.
    """
    current_file = sys.argv[0].split("/")[-1]    # get the running file name
    print(f"Answer to {current_file} is [{answer}] and completed in [{time_taken}]")
