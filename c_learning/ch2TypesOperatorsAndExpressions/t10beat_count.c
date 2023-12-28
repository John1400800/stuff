#include <stdio.h>

unsigned beat_count(unsigned n) {
    unsigned cnt = 0;
    while (n) {
        n &= n - 1u;
        ++cnt;
    }
    return cnt;
}

unsigned beats_to_unsigned(char *source) {
    unsigned res = 0;
    unsigned i = 0;
    while (source[i] == '1' || source[i] == '0') {
        res = res << 1 | (source[i] == '1');
        ++i;
    }
    return res;
}

int main() {
    printf("%d", beat_count(beats_to_unsigned("000001")));
}