// 程序9.5 用scanf()读取字符串
// 此程序演示%s scanf格式字符串

#include <stdio.h>

int main (void)
{
    char s1[81], s2[81], s3[81];
    
    printf ("Enter text:\n");
    
    scanf("%s%s%s", s1, s2, s3);
    
    printf("\ns1 = %s\ns2 = %s\ns3 = %s\n", s1, s2, s3);
    return 0;
}