/*
 * The sum of the squares of the first ten natural numbers is,
 * 
 * 1^2 + 2^2 + ... + 10^2 = 385
 * The square of the sum of the first ten natural numbers is,
 * 
 * (1 + 2 + ... + 10)^2 = 55^2 = 3025
 * Hence the difference between the sum of the squares of the first
 * ten natural numbers and the square of the sum is 3025 − 385 = 2640.
 * 
 * Find the difference between the sum of the squares of the first one
 * hundred natural numbers and the square of the sum.
 */

#include <stdio.h>
#include <math.h>

int maxnum = 100;
int sq = 0;
int sumsq = 0;

int main()
{
    for (int i = 1; i <= maxnum; i ++)
    {
        sq = sq + pow(i, 2);
        sumsq = sumsq + i;
    }
    sumsq = pow(sumsq, 2);
    int diff = sumsq - sq;    

    printf("sq = %d\n", sq);
    printf("sumsq = %d\n", sumsq);
    printf("difference = %d\n", diff);
}

