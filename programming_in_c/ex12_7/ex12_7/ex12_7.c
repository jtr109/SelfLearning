#include <stdio.h>

#define IS_LOWER_CASE(c) ( ((c) >= 'a' && (c) <= 'z') )
#define IS_UPPER_CASE(c) ( ((c) >= 'A' && (c) <= 'Z') )
#define IS_ALPHABETIC(c) ( IS_LOWER_CASE(c) || IS_UPPER_CASE(c) )

int main (void)
{
    printf("'A' = %d\n", IS_ALPHABETIC('A'));
    printf("'m' = %d\n", IS_ALPHABETIC('m'));
    printf("'Z' = %d\n", IS_ALPHABETIC('Z'));
    printf("'1' = %d\n", IS_ALPHABETIC('1'));
    
    return 0;
}