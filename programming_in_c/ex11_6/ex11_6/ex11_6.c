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

int bitpat_search (unsigned int source, unsigned int pattern, int n)
{
    int sizeOfSource, count, index;
    unsigned int mask, partOfPattern, partOfSource;
    int size (unsigned int testNumber);
    
    sizeOfSource = size(source);
    
    for (count = 0, mask = 0; count < n; ++count)
        mask = (mask << 1) | 0x1;
    partOfPattern = pattern & mask;
    
    for (index = 0; index < sizeOfSource - n; ++index) {
        partOfSource = (source >> (sizeOfSource - n - index)) & mask;
        if (partOfSource == partOfPattern)
            return index;
    }
    
    return -1;
}

int main (void)
{
    int index;
    int bitpat_search (unsigned int source, unsigned int pattern, int n);
    
    index = bitpat_search(0xe1f4, 0x5, 3);
    
    printf("index = %d\n", index);
    
    return 0;
}