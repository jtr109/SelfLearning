#include <stdio.h>

void substring (const char source[], int start, int count, char result[])
{
    int i;
    for (i = 0; i < count && source[start+i] != '\0'; i++)
        result[i] = source[start+i];
    result[i] = '\0';
    
    return;
}

int main (void)
{
    void substring (const char source[], int start, int count, char result[]);
    char result[50];
    
    substring("character", 4, 5, result);
    
    printf("%s\n", result);
    
    return 0;
}