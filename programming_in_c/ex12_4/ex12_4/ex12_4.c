#include <stdio.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MAX3(a, b, c) MAX(MAX(a, b), c)
#define SHIFT(value, n) ((n) > 0 ? (value << n) : (value >> -n))

int main (void)
{
    printf("min: %d\n", MIN(1+2, 2));
    printf("max3: %d\n", MAX3(1+2, 2+3, 1+3));
    
    unsigned int w1 = 0177777u, w2 = 0444u;
    
    printf("%o\t%o\n", SHIFT(w1, 5), w1 << 5);
    printf("%o\t%o\n", SHIFT(w1, -6), w1 >> 6);
    printf("%o\t%o\n", SHIFT(w2, 0), w2 >> 0);
    printf("%o\n", SHIFT(SHIFT(w1, -3), 3));
    
    return 0;
}
