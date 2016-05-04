#include <stdio.h>

int main (void)
{
    int test_number = 0x0;
    int high_bit;
    
    test_number = ~test_number;
    
    if (test_number == 0xffffffff) {
        printf("My system is 32 bits.\n");
        high_bit = (test_number >> 32) & 0x1;
        // printf("%x\n", high_bit);
        if (high_bit == 0x1) {
            printf("mathmatic move\n");
        }
        else if (high_bit == 0x0) {
            printf("logical move\n");
        }
        else {
            printf("What's wrong!!\n");
        }
    }
    else if (test_number == 0xffffffffffffffff) {
        printf("My system is 64 bits.\n");
    }
    else
        printf("What's wrong!\n");
    
    return 0;
}