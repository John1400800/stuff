#include <stdio.h>
#define ALLOCSIZE 5

char *alloc(int n);
void afree(char *p);

int main(void) {
    char i, *p2, *p1 = alloc(3);

    for (i = 0; i < 3; ++i) 
        *(p1+i) = 9;
    
    p2 = alloc(2);
    for (i = 0; i < 2; ++i) 
        *(p2+i) = 8;
    
    for (i = 0; i < ALLOCSIZE; ++i) 
        printf("%d", *(p1+i));
    putchar('\n');
    
    afree(p1+2);
    p2 = alloc(2);
    for (i = 0; i < 2; ++i)
        *(p2+i) = 7;
    
    for (i = 0; i < ALLOCSIZE; ++i) 
        printf("%d", *(p1+i));
        
}

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf;

char *alloc(int n) {
    if (allocp - allocbuf + n <= ALLOCSIZE)
        return (allocp += n) - n;
    return NULL;
}

void afree(char *p) {
    if (p >= allocbuf && p < allocbuf + ALLOCSIZE)
        allocp = p;
}
