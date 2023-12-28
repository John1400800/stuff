#include <stdio.h>

#define MAXLINE 100

unsigned get_str(char *sbuff, unsigned lim) {
    unsigned i = 0;
    while (i < lim && !((sbuff[i] = (char)getchar()) == '\n' && i > 0 &&
                        sbuff[i - 1] == '\n')) {
        ++i;
    }
    if (i >= lim) {
        sbuff[i] = '\0';
    } else {
        sbuff[i - 1] = '\0';
    }
    return i;
}

// FUNCTIONALITY: Copying a file ***conditionally***
int main() {
    char buff[MAXLINE + 1];
    get_str(buff, MAXLINE);
    printf("%s", buff);
}