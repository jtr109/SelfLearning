#include <stdio.h>

#define IS_UPPER_CASE(c) (((c) >= 'A' && (c) <= 'Z') ? (c-'A') : -1)

int main (void)
{
    printf("A = %d\n", IS_UPPER_CASE('A'));
    printf("M = %d\n", IS_UPPER_CASE('M'));
    printf("Z = %d\n", IS_UPPER_CASE('Z'));
    printf("c = %d\n", IS_UPPER_CASE('c'));
    
    return 0;
}