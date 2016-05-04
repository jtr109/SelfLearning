#include <stdio.h>

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

int main(void)
{
    void removeString(char text[], int start, int count);
    char text[20] = "the wrong son";
    
    removeString(text, 4, 6);
    
    printf("%s\n", text);
    
}