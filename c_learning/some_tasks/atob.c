#include <stdio.h>

unsigned btou(char *s, unsigned base) {
    unsigned i, res;
    res = 0;
    i = 0;
    if (s[i] == '0') {
        base = 8;
        if (s[i+1] == 'x' || s[i+1] == 'X') {
            base = 16;
            ++i;
        }
        ++i;
    }
    while (1) {
        if (s[i] >= '0' && s[i] <= (base < 10 ? '0' + base - 1 : '9')) {
            res = res * base + (unsigned)(s[i] - '0');
        } else if (s[i] >= 'a' && s[i] <= ('a' + base - 11)) {
            res = res * base + 10 + (unsigned)(s[i] - 'a');
        } else {
            if (s[i] != '\0') {
                res = 0;
                printf("err");
            }
            break;
        }
        ++i;
    }
    return res;
}

int main(void) {
    printf("%d %d", btou("0127", 1), 0127);
    return 0;
}
