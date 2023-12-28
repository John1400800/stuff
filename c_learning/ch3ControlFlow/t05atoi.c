#include <stdio.h>

char is_space(char c) { return (c >= 9 && c <= 13) || c == 32; }

int atoi(char *s) {
    int res;
    char sign;
    unsigned i;
    i = 0;
    while (is_space(s[i])) {
        ++i;
    }
    sign = 1;
    if (s[i] == '-' || s[i] == '+') {
        if (s[i] == '-') {
            sign = -1;
        }
        ++i;
    }
    res = 0;
    while (s[i] >= '0' && s[i] <= '9') {
        res = res * 10 + (int)s[i] - '0';
        ++i;
    }
    return sign * res;
}

int main() {
    printf("%d", atoi("-197"));
}
