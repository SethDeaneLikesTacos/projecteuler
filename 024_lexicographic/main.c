/* 
 * A permutation is an ordered arrangement of objects.
 * For example, 3124 is one possible permutation of the
 * digits 1, 2, 3 and 4. If all of the permutations are
 * listed numerically or alphabetically, we call it
 * lexicographic order. The lexicographic permutations
 * of 0, 1 and 2 are:
 * 
 * 012   021   102   120   201   210
 * 
 * What is the millionth lexicographic permutation of
 * the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 */

#include <stdio.h>
#include <stdlib.h>

#define elements 10
#define number 1000000

int num_array[elements];    // numerator digits
int den_array[elements];    // denominator digits
int fac_array[elements];    // factorial digits (this is what we translate to decimal)
int ava_array[elements];    // available numbers to use in the decimal form
int dec_array[elements];    // where the final output is stored


// necessary for qsort
int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}


// calculate factorial
int factorial(int n)
{
    int factorial = 1;
    for (int i = 1; i <= n; i++)
        factorial = factorial * i;
    return factorial;
}


int main()
{
    // fill arrays
    for (int i = elements-1; i >= 0; i--) 
    {
        den_array[i] = factorial(i);
        num_array[i] = (number - 1) % factorial(i+1);
        fac_array[i] = num_array[i] / den_array[i];
        ava_array[i] = i;
    }

    // find decimal value
    for (int i = elements-1; i >= 0; i--) 
    {
        dec_array[i] = ava_array[fac_array[i]];
        ava_array[fac_array[i]] = elements;
        qsort(ava_array, elements, sizeof(int), cmpfunc);

    }

    // print answer
    printf("ANSWER: ");
    for (int j = elements-1; j >= 0; j--)
        printf("%d", dec_array[j]);
    printf("\n");


}

