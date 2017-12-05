/*
 * A palindromic number reads the same both ways. The largest palindrome
 * made from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

#include <stdio.h>

int product = 0;
int max_product = 0;

int main()
{   
    for (int j = 1; j < 1000; j++) {
        for (int k = 1; k < 1000; k++) {
            
            int n, reversedInteger = 0, remainder, originalInteger;

            product = j * k;
            n = product;
            originalInteger = product;

            while( n!=0 )
            {
                remainder = n%10;
                reversedInteger = reversedInteger*10 + remainder;
                n /= 10;
            }
            if (originalInteger == reversedInteger)
                if (product > max_product)
                    max_product = product;
        }
    }
    printf("%d is a palindrome\n", max_product);
}
