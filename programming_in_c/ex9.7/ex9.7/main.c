#include <stdio.h>

void insertString(char text[], char string[], int index)
{
    int lenOfText= 0, lenOfString = 0;
    int i, j;
    
    while (text[lenOfText] != '\0')
        ++lenOfText;                    // count the length of text
    // printf("lenOfText = %i\n", lenOfText);
    while (string[lenOfString] != '\0')
        ++lenOfString;                    // count the length of string
    // printf("lenOfString = %i\n", lenOfString);
    
    // 从text[index]到text[lenOfText]，每个字符向右平移lenOfString个位置；
    for (i = lenOfText; i >= index; --i) {
        text[i+lenOfString] = text[i];
    }
    // printf("text: %s\n", text);
    
    // 从text[index]开始，每个字符替换为string中的字符，直到'\0';
    for (j = 0; string[j] != '\0'; ++j) {
        text[index+j] = string[j];
    }
    
    return;
}

int main (void)
{
    void insertString(char text[], char string[], int index);
    char text[30] = "the wrong son.";
    
    insertString(text, "per", 10);
    
    printf("%s\n", text);
    
    return 0;
}