#include <stdio.h>

unsigned str_len(char *s) {
    unsigned i = 0;
    while (s[i] != '\0') {
        ++i;
    }
    return i;
}

void reverse_str(char *s) {
    char buff;
    int low, high;
    for (low = 0, high = str_len(s) - 1; low < high; ++low, --high) {
        buff = s[high];
        s[high] = s[low];
        s[low] = buff;
    }
}

int main() {
    char s[] = "hello world";
    reverse_str(s);
    printf("%s", s);
}
