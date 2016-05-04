#include <stdio.h>

#define ABSOLUTE_VALUE(x) ( (x) < 0 ? -(x) : (x) )

int main (void)
{
    for (int i = -10; i < 11; ++i) {
        printf("|%d| = %d\n", i, ABSOLUTE_VALUE(i));
    }
    
    return 0;
}