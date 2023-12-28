#include <stdio.h>

#define MAXLINE 100

// worked only in ascii encoding
char is_space(char c) { return (c >= 9 && c <= 13) || c == 32; }

unsigned get_str(char *s, unsigned lim) {
    unsigned i = 0;
    while (i < lim &&
           !((s[i] = (char)getchar()) == '\n' && i > 0 && s[i - 1] == '\n')) {
        ++i;
    }

    if (s[i - 1] == '\n' && s[i] == '\n') {
        --i;
    }
    s[i] = '\0';
    return i;
}

unsigned world_count(char *s) {
    unsigned countr = 0;
    char islastsp = 1;
    unsigned i = 0;
    while (s[i] != '\0') {
        if (is_space(s[i])) {
            islastsp = 1;
        } else if (islastsp == 1) {
            islastsp = 0;
            ++countr;
        }
        ++i;
    }
    return countr;
}

int main(void) {
    char s[MAXLINE + 1];

    printf("input str: ");
    while (!get_str(s, MAXLINE)) {
        printf("try again: ");
    }
    

    printf("input str has %d words", world_count(s));
}
