#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>

#ifndef _CTYPE_H
#define islower(c) ((unsigned)(c)-'a' < 26)
#define toupper(c) (islower(c)? (c) & 0x5f : (c))
#endif // _CTYPE_H

#define BUFFSIZE 256


int main(void) {
    char *buff = malloc(BUFFSIZE+1);
    fgets(buff, BUFFSIZE, stdin);
    for (const char *ptr = buff; *ptr != '\0'; ++ptr)
        putchar(toupper(*ptr));
    putchar('\n');
    return EXIT_SUCCESS;
}
