#include <stdio.h>
#include "get_num.h"

#define MAXLINE 100

unsigned binomial(unsigned, unsigned);

int main(void) {
    unsigned i, j;
    char buff[MAXLINE + 1];

    printf("enter number: ");
    getline(buff, MAXLINE);
    while (!isint(buff)) {
        printf("try again: ");
        getline(buff, MAXLINE);
    }
    for (i = (unsigned)atoi_(buff); i > 0; --i) {
        for (j = i; j > 0; --j) {
            printf("C(%3d, %3d) = %4d\n", i, j, binomial(i, j));
        }
    }
}

unsigned binomial(unsigned n, unsigned m) {
    return (n == m || m == 0) ? 1 : binomial(n - 1, m - 1) + binomial(n - 1, m);
}
