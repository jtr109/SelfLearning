#include <stdio.h>

void concat (char result[], const char str1[], const char str2[])
{
    int i, j;
    
    // printf("%s\n", str1);
    // printf("%s\n", str2);
    
    for (i = 0; str1[i] != '\0'; ++i)
        result[i] = str1[i];
    
    for (j = 0; str2[j] != '\0'; ++j) {
        // printf("%c", str2[j]);
        result[i + j] = str2[j];
    }
    // printf("\n");
    // ++j at the end of for loop
    
    result[i+j] = '\0';
}


int main(void)
{
    void concat (char result[], const char str1[], const char str2[]);
    const char s1[] = {"Test "};
    const char s2[] = {"works."};
    char s3[20];
    
    concat(s3, s1, s2);
    
    printf("%s\n", s3);
    
    return 0;
}