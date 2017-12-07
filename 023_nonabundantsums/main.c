/* 
 * A perfect number is a number for which the sum of its proper
 * divisors is exactly equal to the number. For example, the sum
 * of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
 *    which means that 28 is a perfect number.
 * 
 * A number n is called deficient if the sum of its proper divisors
 * is less than n and it is called abundant if this sum exceeds n.
 * 
 * As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
 *    the smallest number that can be written as the sum of two
 *    abundant numbers is 24. By mathematical analysis, it can be
 *    shown that all integers greater than 28123 can be written as
 *    the sum of two abundant numbers. However, this upper limit
 *    cannot be reduced any further by analysis even though it is
 *    known that the greatest number that cannot be expressed as
 *    the sum of two abundant numbers is less than this limit.
 * 
 * Find the sum of all the positive integers which cannot be written
 * as the sum of two abundant numbers.
 */

#include <stdio.h>
#define max 28123

int sumdivisors;
int abundantarray[max];
int sum = 0;


int isabundantsum(int number)
{
    int k, n;
    for (k = number; k > 0; k--)
    {
        n = number;
        n -= abundantarray[k];
        if (abundantarray[n] != 0)
            return 1;
    }
    return 0;
}


int main()
{
    int i, j;
    for (i = 0; i < max; i++)
    {
        sumdivisors = 0;
        for (j = i/2; j > 0; j--)
        {
            if (i % j == 0)
                sumdivisors += j;
        }

        // if i is abundant
        if (sumdivisors > i)
            abundantarray[i] = i;
        
        if (isabundantsum(i) == 0)
            sum += i;

    }
    printf("ANSWER: %d\n", sum);
}




