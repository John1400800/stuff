#include <stdio.h>

// squeeze: removes all c from s
void squeeze(char *source, char c) {
    unsigned i, j;
    i = j = 0;
    while (source[i] != '\0') {
        if (source[i] != c) {
            source[j++] = source[i];
        }
        ++i;
    }
    source[j] = '\0';
}

int main() {
    char s[] = "helly world";
    squeeze(s, 'l');
    printf("%s", s);
}
