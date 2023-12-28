#include <stdio.h>
#include <ctype.h>

void rtrim(char *source) {
    int end_idx = 0;
    while (source[end_idx] != '\0') {
        ++end_idx;
    }
    --end_idx;
    while (end_idx >= 0 && isspace(source[end_idx])) {
        --end_idx;
    }
    source[end_idx+1] = '\0';
}

void ltrim(char *source) {
    unsigned i, j;
    for (i = 0; isspace(source[i]); ++i) {
        ;
    }
    for (j = 0; (source[j] = source[i + j]) != '\0'; j++) {
        ;
    }
}

void foo(int *s) {
    printf("%d", s[0]);
}

int main() {
    char s[] = "    hello    ";
    
    ltrim(s);
    rtrim(s);
    printf("|%s|", s);
}
