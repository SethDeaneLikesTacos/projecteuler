/*
 * If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 * then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 * 
 * If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
 * words, how many letters would be used?
 * 
 * 
 * NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
 * contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
 * "and" when writing out numbers is in compliance with British usage.
 */

#include <stdio.h>

int sum = 0;
int lastsum = 0;
int one, teen, ten, hun;

int identify_ones(int n)
{
    if (n == 1 || n == 2 || n == 6)
        sum += 3;
    if (n == 4 || n == 5 || n == 9)
        sum += 4;
    if (n == 3 || n == 7 || n == 8)
        sum += 5;
}

int identify_teens(int n)
{
    if (n == 10)
        sum += 3;
    if (n == 11 || n == 12)
        sum += 6;
    if (n == 15)
        sum += 7;
    if (n == 13 || n == 14)
        sum += 8;
}


int identify_tens(int n)
{
    if (n == 1)
        sum += 4;
    if (n == 4 || n == 5 || n == 6)
        sum += 5;
    if (n == 2 || n == 3 || n == 8 || n == 9)
        sum += 6;
    if (n == 7)
        sum += 7;
}



int main()
{
    for (int i = 1; i <= 1000; i ++)
    {

        one = (i % 10) / 1;
        ten = (i % 100) / 10;
        teen = (ten * 10) + one;
        hun = (i % 1000) / 100;

        // 1000
        if (i == 1000)
            sum += 11;

        // hundreds place taking and into account
        if (hun != 0 && ten == 0 && one == 0)
        {
            identify_ones(hun);
            sum += 7;
        }
        if (hun != 0 && (ten != 0 || one != 0))
        {
            identify_ones(hun);
            sum += 10;
        }
        
        // 10-15, above 15, 18 is a weird case
        if (10 <= teen && teen <= 15)
            identify_teens(teen);
        if (teen > 15 && teen != 18) 
        {
            identify_tens(ten);
            identify_ones(one);
        }
        if (teen == 18)
            sum += 8;

        // ones place
        if (ten == 0)
            identify_ones(one);

        printf("i = %d  :  letters = %d  :  sum = %d\n",i, sum - lastsum, sum);
        lastsum = sum;
    }
}


