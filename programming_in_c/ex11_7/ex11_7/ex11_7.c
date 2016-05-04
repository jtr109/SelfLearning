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

unsigned int bitpat_get (unsigned int source, int index, int n)
{
    unsigned int partOfSource, mask;
    int sizeOfSource, count;
    int size (unsigned int testNumber);
    
    sizeOfSource = size(source);
    for (count = 0, mask = 0; count < n; ++count)
        mask = (mask << 1) | 0x1;
    partOfSource = (source >> (sizeOfSource - index - n)) & mask;
    
    return partOfSource;
}

int main (void)
{
    unsigned int x;
    x = 0xe1f4;
    printf("%x\n", bitpat_get(x, 0, 3));
    printf("%x\n", bitpat_get(x, 3, 6));
    
    return 0;
}