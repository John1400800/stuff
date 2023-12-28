#include <ctype.h>
#include <stdio.h>

unsigned getint(int *n) {
    *n = 0;
    unsigned pos = 0;
    char curr_c, is_valid = 1, is_minus = 0;
    while ((curr_c = (char)getchar()) != '\n') {
        if (!isdigit(curr_c) && !(pos == 0 && curr_c == '-')) {
            is_valid = 0;
        } else if (is_valid && curr_c != '-') {
            *n = *n * 10 + curr_c - '0';
        } else if (curr_c == '-') {
            is_minus = 1;
        }
        ++pos;
    }
    if (is_minus) {
        *n *= -1;
    }
    if (is_valid && pos != 0 && !(is_minus && pos == 1)) {
        return pos;
    }
    return 0;
}

int main(void) {
    int n;
    printf("enter a number: ");
    while (!getint(&n)) {
        printf("try again: ");
    }
    printf("%d", n);
    
    return 0;
}
