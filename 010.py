import pef
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def main():
    pef.answer(sum(pef.prime_sieve(2000000)))

main()
    
