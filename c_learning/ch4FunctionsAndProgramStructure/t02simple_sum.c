#include <stdio.h>

#define MAXLINE 100

signed char get_num(char *source, unsigned lim);
double atof(char *source);

int main(void) {
    char s[MAXLINE + 1];
    signed char is_dig;
    double sum;
    sum = 0;
    printf("input numbers:\n");
    while ((is_dig = get_num(s, MAXLINE))) {
        if (is_dig == -1) {
            printf("input again: ");
        } else {
            sum += atof(s);
        }
    }
    printf("%lf", sum);
}

unsigned char is_digit(char c) { return c >= '0' && c <= '9'; }

double atof(char *source) {
    unsigned i = 0;
    int res = 0;
    int pow = 0;
    int sign = 1;

    if (source[i] == '-' || source[i] == '+') {
        if (source[i] == '-') {
            sign *= -1;
        }
        ++i;
    }
    while ((source[i] >= '0' && source[i] <= '9') || source[i] == '.') {
        if (source[i] == '.') {
            pow = 1;
        } else {
            res = res * 10 + (int)source[i] - '0';
            pow *= 10;
        }
        ++i;
    }
    return (double)(sign * res) / (double)(pow ? pow : 1);
}

signed char get_num(char *s, unsigned lim) {
    unsigned i = 0;
    signed char is_dig = 1;
    unsigned char is_dot = 0;
    while (i < lim && (s[i] = (char)getchar()) != '\n') {
        if (!is_digit(s[i]) && !(s[i] == '-' && i == 0) && !(s[i] == '.' && !is_dot)) {
            is_dig = -1;
        }
        if (s[i] == '.') {
            is_dot = 1;
        }
        ++i;
    }
    s[i] = '\0';
    if (i == 0 || (i == 1 && (s[0] == '-' || s[0] == '.')) || (i == 2 && s[0] == '-' && s[1] == '.')) {
        if (i == 0) {
            return 0;
        }
        return -1;
    }
    return is_dig;
}
