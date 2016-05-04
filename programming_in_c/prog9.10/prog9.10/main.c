#include <stdio.h>
#include <stdbool.h>

struct entry1
{
    char word[15];
    char definition[50];
};

/*
bool equalStrings (const char s1[], const char s2[])
{
    int i = 0;
    bool areEqual;
    
    while ( s1[i] ==  s2[i] &&
           s1[i] != '\0' && s2[i] != '\0')
        ++i;
    
    if (s1[i] == '\0' && s2[i] == '\0')
        areEqual = true;
    else
        areEqual = false;
    
    return areEqual;
}
*/

int compareStrings (const char s1[], const char s2[])
{
    int i = 0, answer;
    
    while (s1[i] == s2[i] &&  s1[i] != '\0' && s2[i] != '\0')
        ++i;
    
    if (s1[i] < s2[i])
        answer = -1;
    else if (s1[i] == s2[i])
        answer = 0;
    else
        answer = 1;
    
    return answer;
}

// find a word in dictionary
int lookup (const struct entry1 dictionary[], const char search[],
            const int entries)
{
    int low = 0;
    int high = entries -1;
    int mid, result;
    int compareStrings (const char s1[], const char s2[]);
    
    while (low <= high) {
        mid = (low + high) / 2;
        result = compareStrings(dictionary[mid].word, search);
        
        if (result == -1)       // s1 < s2
            low = mid + 1;
        else if (result == 1)   // s1 > s2
            high = mid -1;
        else                    // s1 == s2
            return mid;
    }
    
    return -1;
}

int main (void)
{
    const struct entry1 dictionary[100] = {
        {"aardvark", "a burrowing African mammal"       },
        {"abyss",    "a bottomless pit"                 },
        {"acumen",   "muentally sharp; keen"            },
        {"addle",    "to become confused"               },
        {"aerie",    "a high nest"                      },
        {"affix",    "to append; attach"                },
        {"agar",     "a jelly made from seaweed"        },
        {"ahoy",     "a nautical call of greeting"      },
        {"aigrette", "an ornamental cluster of feathers"},
        {"ajar",     "partially opened"                 } };
    
    char word[10];
    int entries = 10;
    int entry2;
    int lookup (const struct entry1 dictionary[], const char search[],
                const int entries);
    
    printf("Enter word: ");
    scanf("%14s", word);
    entry2 = lookup(dictionary, word, entries);
    
    if (entry2 != -1)
        printf("%s\n", dictionary[entry2].definition);
    else
        printf("Sorry, the word %s is not in my dictionary.\n", word);
    
    return 0;
}