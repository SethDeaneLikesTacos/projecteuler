/* 
 * Let d(n) be defined as the sum of proper divisors of n
 * (numbers less than n which divide evenly into n).
 * If d(a) = b and d(b) = a, where a ≠ b, then a and b are
 * an amicable pair and each of a and b are called amicable numbers.
 * 
 * For example, the proper divisors of 220 are 1, 2, 4, 5, 10,
 * 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper
 * divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
 * 
 * Evaluate the sum of all the amicable numbers under 10000.
 */

#include <stdio.h>
int max = 10000;
int sum = 0;

int main()
{
    int i, j, k;
    int pair, pair2;

    for (i = 0; i <= max; i ++)
    {
        pair = 0;
        pair2 = 0;
        for (j = i/2; j > 0; j--)
        {
            if (i % j == 0)
                pair += j;
        }



        for (k = pair/2; k > 0; k--)
        {
            if (pair % k == 0)
                pair2 += k;
        }

        if (i == pair2 && pair != pair2)
        {
            printf("%d,   %d   %d\n", i, pair, pair2);
            sum += i;
        }
       
    }
    printf("ANSWER: %d\n", sum);
}
