#include <stdio.h>
/*

<type> *p;
p = &a[0] ~ p = a

&a[i] ~ &*(a+i) ~ a+i
&a[0] ~ &*(a+0) ~ a+0 ~ a

*/
#define BUFFSIZE 3

static char cbuff[BUFFSIZE];
static char *cbuffp = cbuff;

char getch(void) {
    return cbuffp > cbuff ? *--cbuffp : getchar();
}

void ungetch(char c) {
    if (cbuffp < cbuff + BUFFSIZE)
        *cbuffp++ = c;
    else
        printf("\nungetc: cbuff overflow\n");
}

