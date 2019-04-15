import resources.pef as pef
import time
"""
https://projecteuler.net/problem=108
"""

def main():
    
    return pef.is_prime(3)

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)