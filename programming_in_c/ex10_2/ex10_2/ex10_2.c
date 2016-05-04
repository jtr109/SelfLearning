#include <stdio.h>

struct entry1 {
    int value;
    struct entry1 *next;
};

void insertEntry (struct entry1 *newEntry, struct entry1 *frontEntry)
{
    newEntry->next = frontEntry->next;
    frontEntry->next = newEntry;
}

void removeEntry (struct entry1 *frontEntry)
{
    frontEntry->next = (*frontEntry).next->next;
}

void displayEntry (struct entry1 *listPtr)
{
    while (listPtr != (struct entry1 *) 0) {
        printf("%i  ", listPtr->value);
        listPtr = listPtr->next;
    }
    printf("\n");
}

int main (void)
{
    
    struct entry1 n1, n2, n3, n4, n5;
    struct entry1 *listStart;
    void displayEntry (struct entry1 *listPtr);
    void removeEntry (struct entry1 *frontEntry);
    void insertEntry (struct entry1 *newEntry, struct entry1 *frontEntry);
    
    n1.value = 100;
    // n1.front = 0;
    n1.next = &n2;
    
    n2.value = 200;
    // n2.front = &n1;
    n2.next = &n3;
    
    n3.value = 300;
    // n3.front = &n2;
    n3.next = &n4;
    
    n4.value = 400;
    // n4.front = &n3;
    n4.next = 0;
    
    n5.value = 500;
    n5.next = 0;
    
    listStart = &n1;
    
    displayEntry (listStart);
    
    removeEntry (&n2);
    displayEntry (listStart);
    // succeed
    
    insertEntry (&n3, &n2);
    insertEntry (&n5, &n4);
    displayEntry (listStart);
    
    
    return 0;
}