/*
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 * 
 * a^2 + b^2 = c^2
 * For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
 * 
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 */

#include <stdio.h>
#include <math.h>

int sum = 1000;

int main()
{
    for (int a = 1; a < sum / 2; a++) {
        for (int b = 1; b < sum / 2; b++)
        {
            int c = pow(pow(a,2) + pow(b,2),.5);
            int hyp = pow(a,2) + pow(b,2);

            if (a+b+c == sum && pow(hyp,.5) == c && a<b && b<c)
                printf("%d\n", a*b*c);
        }
    }
}
