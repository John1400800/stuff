#include <stdio.h>

void lower(char *source) {
    unsigned i = 0;
    while (source[i] != '\0') {
        if (source[i] >= 'A' && source[i] <= 'Z') {
            source[i] += 'a' - 'A';
        }
        ++i;
    }
}

int main() {
    char s[] = "HELLO!";
    lower(s);
    printf("%s", s);
}