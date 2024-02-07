#include <stdio.h>

#ifndef _INC_CTYPE
#define isspace(c) (((c) >= 9 && (c) <= 13) || (c) == 32)
#define isdigit(c) ((c) >= '0' && (c) <= '9')
#endif

int get_int(int *res);
#ifdef _INC_STDIO
#define get_int(num, welcm_msg, error_msg)                                     \
    printf(welcm_msg);                                                         \
    while (!get_int(&(num)))                                                   \
        printf(error_msg);
#endif

int main(void) {
    int n;
    get_int(n, "enter a integer: ", "try again: ");
    printf("%d", n);
    return 0;
}

#ifdef get_int
#undef get_int
#endif
// if entered is a number, return 1, otherwise 0; the result write in res
int get_int(int *res) {
    int c, sign, is_dig, first;
    sign = 1;
    do
        c = getchar();
    while (c != '\n' && isspace(c)); // skip the remaining spaces
    if (c == '-' || c == '+') {      // get sign
        if (c == '-')
            sign = -1;
        c = getchar();
    }
    for (*res = 0, is_dig = 1, first = 1; c != '\n'; c = getchar(), first = 0)
        if (is_dig && (is_dig = isdigit(c)))
            *res = (*res * 10) + (c - '0');
    *res *= sign;
    return !first && is_dig;
}
