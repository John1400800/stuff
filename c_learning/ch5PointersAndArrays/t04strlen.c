#include <stdio.h>

int str_len1(char *s) {
    char *p = s;
    while (*(p++) != '\0')
        ;
    return (int)(p-s)-1;
}

int main(void) {
    printf("%d", str_len1("hello"));
    return 0;
}
