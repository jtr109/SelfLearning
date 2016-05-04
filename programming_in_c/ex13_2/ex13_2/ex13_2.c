#include <stdio.h>

int main (void)
{
    
    int days;
}

char* monthName (int n)
{
    char *namePtr;
    enum month {January = 1, February, March, April, May, June,
        July, August, September, October, November, December};
    enum month aMonth;
    namePtr = # &aMonth;
    switch (aMonth) {
        case January:
        case March:
        case May:
        case July:
        case August:
        case October:
        case December:
            days = 31;
            break;
        case April:
        case June:
        case September:
        case November:
            days = 30;
            break;
        case February:
            days = 28;
            break;
        default:
            printf("bad month number\n");
            days = 0;
            break;

}