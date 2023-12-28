#include <stdio.h>

unsigned str_length(char *str) {
    unsigned i = 0;
    while (str[i] != '\0') {
        ++i;
    }
    return i;
}

int rstr_index(char *source, char *sub) {
    int i, j;
    int sub_maxj = (int)str_length(sub) - 1;

    for (i = (int)str_length(source) - 1; i >= 0; --i) {
        for (j = sub_maxj; j >= 0 && (i - sub_maxj + j) >= 0; --j) {
            if (sub[j] != source[i - sub_maxj + j]) {
                break;
            }
        }
        if (j < 0) {
            return i;
        }
    }
    return -1;
}

int main(void) { printf("%d", rstr_index("orldy", "worldy")); }
