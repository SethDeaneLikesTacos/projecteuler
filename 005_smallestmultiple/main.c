/*
 * 2520 is the smallest number that can be divided by each of
 * the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible
 * by all of the numbers from 1 to 20?
 */

#include <stdio.h>

int divisors = 20;
int max = 999999999;
int found = 0;

int main()
{
    int i = 1;
    for (i; i < max; i++){
        for (int j = 1; j <= divisors; j++)
        {
            if (j == divisors && i % j == 0)
                {printf("%d\n", i);
                found = 1;
                break;}
            if (i % j == 0)
                {continue;}
            else
                {break;}
        }
    if (found == 1)
        break;
    }
}
