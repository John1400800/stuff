#include <stdio.h>

unsigned htou(char *source) {
    unsigned res = 0;
    unsigned pos = 0;
    while (source[pos] >= '0' && source[pos] >= '0' ||
           source[pos] >= 'a' && source[pos] <= 'f') {
        res = res * 16 + (source[pos] >= '0' && source[pos] <= '9'
                              ? source[pos] - '0'
                              : source[pos] - 'a' + 10);
        ++pos;
    }
    return res;
}

int main() {
    printf("%d", htou("1fa"));
}