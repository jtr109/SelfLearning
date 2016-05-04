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

void bitpat_set (unsigned int *sourcePtr, unsigned int pattern, int index, int n)
{
    int size (unsigned int testNumber);
    unsigned int mask;
    int sizeOfSource, count;
    
    sizeOfSource = size (*sourcePtr);
    
    for (count = 0, mask = 0; count < n; ++count)
        mask = (mask << 1) | 0x1;
    *sourcePtr &= ~(mask << (sizeOfSource - index - n));
    *sourcePtr |= (pattern << (sizeOfSource - index -n));
}

int main (void)
{
    unsigned int x = 0xe1f4;
    bitpat_set(&x, 0, 2, 5);
    printf("%x\n", x);
    bitpat_set(&x, 0x55u, 0, 8);
    printf("%x\n", x);
    
    return 0;
}