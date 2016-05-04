#include <stdio.h>

int size (unsigned int testNumber)
{
    int count = 0, temp = 0x0;
    
    while (temp < testNumber) {
        ++count;
        temp = (temp << 1) | 0x1;
    }
    // printf("size of testNumber is %i\n", count);
    
    return count;
}

int bit_test (unsigned int testNumber, int n)
{
    int sizeOfNumber, nBit;
    int size (unsigned int testNumber);
    
    sizeOfNumber = size(testNumber);
    n %= sizeOfNumber;
    nBit = (testNumber >> (sizeOfNumber - n - 1)) & 0x1;
    
    return nBit;
}

unsigned int bit_set (unsigned int testNumber, int n)
{
    int mask = 1, sizeOfNumber, newNumber;
    int size (unsigned int testNumber);
    
    sizeOfNumber = size(testNumber);
    n %= sizeOfNumber;
    
    while (sizeOfNumber - n - 1 > 0) {
        mask = (mask << 1) & (~0x1);
        ++n;
    }
    newNumber = testNumber | mask;
    
    return newNumber;
}

int main (void)
{
    int bit_test (unsigned int testNumber, int n);
    
    printf ("%d\n", bit_test(0xa, 0));
    printf ("%d\n", bit_test(0xa, 1));
    printf ("%d\n", bit_test(0xa, 2));
    printf ("%d\n", bit_test(0xa, 3));
    
    printf ("%x\n", bit_set(0xa, 1));
    
    return 0;
}