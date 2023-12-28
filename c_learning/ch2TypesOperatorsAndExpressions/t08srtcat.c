#include <stdio.h>

void strcat_(char *s, char *t) {
    unsigned i, j;
    i = j = 0;
    while (s[i] != '\0') {
        ++i;
    }
    while ((s[i++] = t[j++]) != '\0') {
        ;
    }
}

int main() {
    char s[100] = "hello";
    strcat_(s, " world");
    printf("%s", s);
}
