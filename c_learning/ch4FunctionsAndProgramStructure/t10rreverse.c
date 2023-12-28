#include <stdio.h>

#define swap(type, a, b)                                                       \
    type term = a;                                                             \
    a = b;                                                                     \
    b = term

unsigned str_len(char *s) {
    unsigned i = 0;
    while (s[i] != '\0') {
        ++i;
    }
    return i;
}

void preverse(char *source, unsigned i) {
    if (source[i] != '\0') {
        preverse(source, i + 1);
        putchar(source[i]);
    }
}

void reverse(char *s, unsigned start, unsigned end) {
    if (start < end) {
        swap(char, s[start], s[end]);
        reverse(s, start + 1, end - 1);
    }
}

int main(void) {
    char s[] = "hello";

    reverse(s, 0, str_len(s) - 1);
    printf("%s\n", s);
    preverse(s, 0);
    return 0;
}
