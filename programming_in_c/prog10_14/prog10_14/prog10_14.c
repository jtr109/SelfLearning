// 此函数将一个字符串复制给另一个字符串，指针第2版

#include <stdio.h>

void copyString (char *to, char *from)
{
    while (*from)
        *to++ = *from++;
    
    *to = '\0';
}

int main (void)
{
    void copyString (char *to, char *from);
    char string1[] = "A string to be copied.";
    char string2[50];
    
    copyString(string2, string1);
    printf("%s\n", string2);
    
    copyString(string2, "So is this.");
    printf("%s\n", string2);
    
    return 0;
}
