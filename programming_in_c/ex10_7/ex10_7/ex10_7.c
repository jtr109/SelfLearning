#include <stdio.h>

void sort (int *array, int n)
{
    int *arrayI, *arrayJ;
    int temp;
    for (arrayI = array; arrayI < array + n - 1; ++arrayI)
        for (arrayJ = arrayI + 1; arrayJ < array + n; ++arrayJ)
            if (*arrayI > *arrayJ) {
                temp = *arrayI;
                *arrayI = *arrayJ;
                *arrayJ = temp;
            }
}

int main (void)
{
    int array[16] = {34, -5, 6, 0, 12, 100, 56, 22,
        44, -3, -9, 12, 17, 22, 6, 11};
    int *arrayPtr;
    void sort (int *array, int n);
    
    printf("The array before the sort:\n");
    
    for (arrayPtr = array; arrayPtr < array + 16; ++arrayPtr)
        printf("%i ", *arrayPtr);
    
    sort(array, 16);
    
    printf("\n\nThe array after the sort:\n");
    
    for (arrayPtr = array; arrayPtr < array + 16; ++arrayPtr)
        printf("%i ", *arrayPtr);
    
    printf("\n");
    
    return 0;
}