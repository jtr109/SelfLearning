#include <stdio.h>

struct entry1 {
    int value;
    struct entry1 *front;
    struct entry1 *next;
};

void displayEntry (struct entry1 *listPtr)
{
    while (listPtr != (struct entry1 *) 0) {
        printf("%i  ", listPtr->value);
        listPtr = listPtr->next;
    }
    printf("\n");
}

void insertEntry (struct entry1 *newEntry, struct entry1 *frontEntry, struct entry1 *nextEntry)
{
    if (frontEntry != (struct entry1 *) 0) {
        newEntry->next = frontEntry->next;
        frontEntry->next = newEntry;
    } else if (nextEntry != (struct entry1 *) 0) {
        newEntry->front = nextEntry->front;
        nextEntry->front = newEntry;
    }
}

void removeEntry (struct entry1 *thisEntry)
{
    if (thisEntry->next != (struct entry1 *) 0) {
        thisEntry->next->front = thisEntry->front;
    }
    if (thisEntry->front != (struct entry1 *) 0) {
        thisEntry->front->next = thisEntry->next;
    }
}

int main (void)
{
    
    struct entry1 n1, n2, n3, n4;
    struct entry1 *listStart;
    void displayEntry (struct entry1 *listPtr);
    void insertEntry (struct entry1 *newEntry, struct entry1 *frontEntry, struct entry1 *nextEntry);
    void removeEntry (struct entry1 *thisEntry);
    
    n1.value = 100;
    n1.front = 0;
    n1.next = &n2;
    
    n2.value = 200;
    n2.front = &n1;
    n2.next = &n3;
    
    n3.value = 300;
    n3.front = &n2;
    n3.next = &n4;
    
    n4.value = 400;
    n4.front = &n3;
    n4.next = 0;
    
    listStart = &n1;
    
    displayEntry(listStart);
    
    // remove the first and mid entry
    removeEntry(&n1);
    listStart = &n2;
    removeEntry(&n3);
    displayEntry(listStart);
    
    insertEntry(&n1, 0, &n2);
    listStart = &n1;
    displayEntry(listStart);
    insertEntry(&n3, &n2, &n4);
    displayEntry(listStart);
    
    return 0;
}