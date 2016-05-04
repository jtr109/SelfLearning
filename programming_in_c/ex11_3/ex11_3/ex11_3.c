#include <stdio.h>

int int_size (void)
{
    int n = ~(0x0), count = 0, test_number = 0x0;
    
    // printf("n = %x, n << 32 = %x\n", n, n << 32);
    
    while (n != test_number) {
        ++count;
        test_number = (test_number << 1) | 0x1;
    }
    
    return count;
}

int main (void)
{
    int int_size (void);
    
    printf("int is %i bits.\n", int_size());
    
    return 0;
}