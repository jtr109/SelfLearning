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

unsigned int rotate (unsigned int value, int n)
{
    unsigned int result, bits;
    
    if (n > 0)
        n = n % 32;
    else
        n = -(-n % 32);
    
    if (n == 0)
        result = value;
    else if (n > 0) {
        bits = value >> (32 - n);  // 将移出的高位放在低位
        result = value << n | bits;  // 低位用bits补
    }
    else {
        n = -n;
        bits = value << (32 - n);  // 将会被移出的低位放在高位
        result = value >> n | bits;  // 求或合并
    }
    
    return result;
}