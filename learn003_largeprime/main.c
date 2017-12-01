/*
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 */
 

#include <stdio.h>

unsigned long number = 600851475143;
unsigned long prime = 0;

unsigned long is_prime(unsigned long num)
{
     if (num <= 1) return 0;
     if (num % 2 == 0 && num > 2) return 0;
     for(int i = 3; i < num / 2; i+= 2)
     {
         if (num % i == 0)
             return 0;
     }
     return 1;
}

unsigned long main()
{
    for (unsigned long i = number/2; i >= 0; i = i - 1)
    {
        if (number % i == 0 && is_prime(i))
            printf("PRIME %lu\n", i);
    }
}





