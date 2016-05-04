#include <stdio.h>

int main (void)
{
    unsigned int w1 = 0xabcdef00u, w2 = 0xffff1122u;
    unsigned int rotate (unsigned int value, int n);
    
    printf("%x\n", rotate(w1, 8));
    printf("%x\n", rotate(w1, -16));
    printf("%x\n", rotate(w2, 4));
    printf("%x\n", rotate(w2, -2));
    printf("%x\n", rotate(w1, 0));
    printf("%x\n", rotate(w1, 44));
    
    return 0;
}

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

unsigned int rotate (unsigned int value, int n)
{
    unsigned int result, bits;
    int intSize;
    int int_size (void);
    
    intSize = int_size();
    
    if (n > 0)
        n = n % intSize;
    else
        n = -(-n % intSize);
    
    if (n == 0)
        result = value;
    else if (n > 0) {
        bits = value >> (intSize - n);  // 将移出的高位放在低位
        result = value << n | bits;  // 低位用bits补
    }
    else {
        n = -n;
        bits = value << (intSize - n);  // 将会被移出的低位放在高位
        result = value >> n | bits;  // 求或合并
    }
    
    return result;
}