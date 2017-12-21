import pef
"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():
    maxpal = 0
    for i in range(1000, 1, -1):
        for j in range(1000, 1, -1):
            product = i * j    
            revproduct = pef.reversenum(product) 
            if revproduct == product and product > maxpal:
                maxpal = product

    pef.answer(maxpal)

main()
