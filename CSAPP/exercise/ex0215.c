#include <stdio.h>

int equal(int x, int y) {
    return !(x & ~y);
}

int main (void)
{
    printf("0x3 == 0x5: %.2x\n", equal(0x3, 0x5));
    printf("0x3 == 0x3: %.2x\n", equal(0x3, 0x3));
    printf("0x3fca == 0x3fca: %.2x\n", equal(0x3fca, 0x3fca));

    return 0;
}
