/*
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below two million.
 */

#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

int max = 2000000;
uint64_t sum = 0;
int pc = 0;

int main() 
{
    for (int i = 1; i <= max; i ++)
    {
        // can ignore multiples of 2 and 5, but 2 and 5 are prime
        if (i > 2 && i % 2 == 0 || i > 5 && i % 5 == 0 || i == 1)
            continue;
        else
        {
            pc = 0; // prime check
            for (int j = 1; j < i/2; j = j + 2)
            {
                if (i % j == 0)
                    pc ++;
            }

            if (pc == 1 || i == 2 || i == 3)
                sum = sum + i;
        }
    } 
    printf("sum = %"PRIu64"\n", sum);
}
