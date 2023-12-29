#include <stdio.h>

int str_len1(char *ap) {
    char *sp = ap;
    while (*(ap++) != '\0');
    return (int)(ap-sp) - 1;
}

int main(void) {
    printf("%d", str_len1("hello"));
    return 0;
}
