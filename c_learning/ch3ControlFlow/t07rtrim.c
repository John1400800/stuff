#include <stdio.h>

unsigned str_len(char *s) {
    unsigned i = 0;
    while (s[i] != '\0') {
        ++i;
    }
    return i;
}

char is_space(char c) { return (c >= 9 && c <= 13) || c== 32; }

void rtrim(char *s) {
    int i = str_len(s) - 1; 
    while (i >= 0 && is_space(s[i])) {
        --i;
    }
    s[i + 1] = '\0';
}

int main() {
    char s[] = "hi   ";
    rtrim(s);
    printf("|%s|", s);
}
