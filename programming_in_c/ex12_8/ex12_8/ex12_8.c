#include <stdio.h>

#define IS_LOWER_CASE(x) ( ((x) >= 'a' && (x) <= 'z') )
#define IS_UPPER_CASE(x) ( ((x) >= 'A' && (x) <= 'Z') )
#define IS_ALPHABETIC(x) ( IS_LOWER_CASE(x) || IS_UPPER_CASE(x) )
#define IS_DIGIT(x) ( ((x) >= '0' && (x) <= '9') )
#define IS_SPECIAL(x) ( !IS_ALPHABETIC(x) && !IS_DIGIT(x) )

int main (void)
{
    printf("'A' = %d\n", IS_ALPHABETIC('A'));
    printf("'m' = %d\n", IS_ALPHABETIC('m'));
    printf("'Z' = %d\n", IS_ALPHABETIC('Z'));
    printf("'1' = %d\n", IS_DIGIT('1'));
    printf("'#' = %d\n", IS_SPECIAL('#'));
    
    return 0;
}