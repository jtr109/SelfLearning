#include <stdio.h>
#include <stdbool.h>

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

int findString (char source[], char substring[])
{
    int i, j;
    bool match = false;
    
    for (i = 0; source[i] != '\0'; ++i) {
        if (source[i] == substring[0]) {
            match = true;
            for (j = 0; substring[j] != '\0' && match == true; ++j) {
                if (source[i+j] != substring[j])
                    match = false;
            }
        }
        if (match == true)
            return i;
    }
    
    return -1;
}

void removeString(char text[], int start, int count)
{
    int lenOfText;
    int i;
    
    while (text[lenOfText] != '\0')
        ++lenOfText;                    // count the length of text

    // 从text[start+count]到字符串尾,每个字符赋值给从text[start]起对应的位置;
    for (i = 0; text[start+count+i] != '\0'; ++i) {
        text[start+i] = text[start+count+i];
    }
    text[start+i] = '\0';
}

bool replaceString (char source[], char s1[], char s2[])
{
    int findString (char source[], char substring[]);
    void removeString (char text[], int start, int count);
    void insertString (char text[], char string[], int index);
    int start = -1, count = 0;
    bool found = false;
    
    // find the index of the first character of s1
    start = findString(source, s1);
    // printf("start = %i\n", start);
    if (start != -1) {
        found = true;
        
        // count the length of s1
        while (s1[count] != '\0') {
            ++count;
        }
        // printf("count = %i\n", count);
        // printf("source before removeString: %s\n", source);
        removeString(source, start, count);
        // printf("source after removeString: %s\n", source);
        
        insertString(source, s2, start);
        // printf("source: %s\n", source);
    }
        
    return found;
}

int main (void)
{
    bool replaceString (char source[], char s1[], char s2[]);
    char text[50] = "bu*y 1p*ass*word *1 t*ime";
    bool stillFound;
    
    do {
        stillFound = replaceString (text, "*", "");
        // printf("%s\n", text);
    }
    while (stillFound);
    
    printf("%s\n", text);
}