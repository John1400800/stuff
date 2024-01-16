#include <math.h>
#include <stdio.h>

#define MAXLINE 100
#define M_PI 3.14159265358979323846

char is_digit(char c) { return c >= '0' && c <= '9'; }

double atof_(char *s) {
    unsigned i = 0;
    int res = 0;
    int sign = 1;
    int pow = 0;
    if (s[i] == '-' || s[i] == '+') {
        if (s[i] == '-') {
            sign *= -1;
        }
        ++i;
    }
    while (is_digit(s[i]) || s[i] == '.') {
        if (s[i] == '.') {
            pow = 1;
        } else {
            res = res * 10 + s[i] - '0';
            pow *= 10;
        }
        ++i;
    }
    return (double)(sign * res) / (double)(pow ? pow : 1);
}

unsigned get_line(char *buff, unsigned lim) {
    unsigned i = 0;
    while (i < lim && (buff[i] = (char)(getchar())) != '\n') {
        ++i;
    }
    buff[i] = '\0';
    return i;
}

char is_num(char *s) {
    unsigned i = 0;
    char is_dig = 1;
    char is_dot = 0;
    while (s[i] != '\0' && is_dig) {
        if (!is_digit(s[i]) && !(s[i] == '.' && !is_dot) &&
            !(s[i] == '-' && i == 0)) {
            is_dig = 0;
        }
        if (s[i] == '.') {
            is_dot = 1;
        }
        ++i;
    }
    if (is_dig && s[i] == '\0' && i != 0 && !(i == 1 && (s[0] == '.' || s[0] == '-')) &&
        !(i == 2 && s[0] == '-' && s[1] == '.')) {
        return 1;
    }
    return 0;
}

int main(void) {
    char buff[MAXLINE + 1];
    double width, ratio_of_r, square;

    printf("enter the width of the ring (a): ");
    while (1) {
        get_line(buff, MAXLINE);
        if ((is_num(buff))) {
            width = atof_(buff);
            if (width >= 0) {
                break;
            }
        }
        printf("try again: ");
    }
    printf("ratio of radii of circles (b): ");
    while (1) {
        get_line(buff, MAXLINE);
        if ((is_num(buff))) {
            ratio_of_r = atof_(buff);
            if (ratio_of_r >= 1) {
                break;
            }
            break;
        }
        printf("try again: ");
    }

    square = (M_PI * pow(width, 2) * (ratio_of_r + 1)) / (ratio_of_r - 1);
    printf("%lf", square);
}
