#include <stdio.h>
#include <stdbool.h>

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

int main (void)
{
    int findString (char source[], char substring[]);
    int index;
    
    index = findString("a chatterbos", "hat");
    
    printf("%i\n", index);
}