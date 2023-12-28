#include <stdio.h>

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

int main(void) {
    printf("%lf", atof("136.953333"));
}
