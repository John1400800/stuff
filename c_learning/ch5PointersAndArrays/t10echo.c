#include <stdio.h>

#ifndef NULL
#define NULL ((void *)0)
#endif

int main(int argc, char *argv[]) {
    while(--argc > 0)
        printf(argc > 1 ? "%s " : "%s", *++argv);
}
