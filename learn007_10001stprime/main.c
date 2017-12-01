/*
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
 * we can see that the 6th prime is 13.
 * 
 * What is the 10,001st prime number?
 */

#include <stdio.h>

int max = 10001;
int count = 1;    // overall prime count

int main() 
{
    for (int i = 1; count <= max; i ++)
    {
        // can ignore multiples of 2 and 5, but 2 and 5 are prime
        if (i > 2 && i % 2 == 0 || i > 5 && i % 5 == 0 || i == 1)
            continue;
        else
        {
            int pc = 0; // prime check
            printf("Checking %d for primeness\n", i);
            for (int j = 1; j < i/2; j = j + 2)
            {
                if (i % j == 0)
                    pc ++;
            }

            if (pc == 1 || i == 2 || i == 3)
                {
                    printf("%d is the %dth prime\n\n", i, count);
                    count++;
                }
        }
    } 
}
