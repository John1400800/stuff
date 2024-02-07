#include <stdio.h>

#define MAXLINE 100
#define is_digit(c) ((c) >= '0' && (c) <= '9')


unsigned get_line(char *s, unsigned lim) {
    unsigned i = 0;
    while (i < lim && (s[i] = (char)getchar()) != '\n') {
        ++i;
    }
    s[i] = '\0';
    return i;
}

int is_valid(char *s) {
    int f = 1;
    unsigned i;
    for (i = 0; f && s[i] != '\0'; ++i) {
        if (!is_digit(s[i])) {
            f = 0;
        } 
    }
    return i > 0 ? f : 0;
}

unsigned atou(char *s) {
    unsigned i, res;
    res = 0;
    for (i = 0; is_digit(s[i]); ++i) {
        res = res * 10 + (unsigned)s[i] - '0';
    }
    return res;
}

int is_prime(unsigned n) {
    unsigned m;
    for (m = 2; m * m <= n; ++m) {
        if (n % m == 0) {
            return 0;
        }
    }
    return n >= 2;
}

int main(void) {
    char buff[MAXLINE + 1];
    for(;;) {
        get_line(buff, MAXLINE);
        if (!is_valid(buff)) {
            printf("try again: ");
            continue;
        }
        printf("%s\n", is_prime(atou(buff)) ? "true" : "false");
    }
}
