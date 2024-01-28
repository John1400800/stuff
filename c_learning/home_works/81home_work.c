#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifndef isdigit
#define isdigit(c) ((c) >= '0' && (c) <= '9')
#endif

#ifndef swap
#define swap(t, a, b) t(temp) = (a), (a) = (b), (b) = (temp)
#endif

#ifndef rrand
#define frand(low, high)                                                       \
    ((low) + ((double)rand() / (double)RAND_MAX) * ((high) - (low)))
#endif

#ifndef MAXLINE
#define MAXLINE 1000
#endif

int is_num(char *s, int is_float) {
    unsigned dot = 0, i = 0;
    while (isdigit(s[i]) || (s[i] == '-' && i == 0) ||
           (is_float && !dot && s[i] == '.')) {
        if (s[i] == '.')
            dot = 1;
        ++i;
    }
    if (s[i] == '\0' && i != 0 && !((s[0] == '-' || s[0] == '.') && i == 1) &&
        !(s[0] == '-' && s[1] == '.' && i == 2))
        return 1;
    return 0;
}

unsigned getline_(char *s, unsigned lim) {
    unsigned i = 0;
    while (i < lim && (s[i] = getchar()) != '\n' && s[i] != EOF)
        ++i;
    s[i] = '\0';
    return i;
}

void init_mrtx(unsigned size, float (*mtrx)[size], int rlow, int rhigh) {
    unsigned i, j;
    for (i = 0; i < size; ++i) {
        for (j = 0; j < size; ++j) {
            *(*(mtrx + i) + j) = frand(rlow, rhigh);
        }
    }
}

void print_mtrx(unsigned size, float (*mtrx)[size]) {
    unsigned i, j;
    for (i = 0; i < size; ++i) {
        putchar('|');
        for (j = 0; j < size; ++j) {
            printf("%5.2f", *(*(mtrx + i) + j));
            putchar('|');
        }
        putchar('\n');
    }
    putchar('\n');
}

void swap_rowtocolumn(unsigned k, unsigned size, float (*mtrx)[size]) {
    unsigned i;
    float temp;
    for (i = 0; i < size; ++i) {
        if (i == k)
            continue;
        temp = (*(*(mtrx + k) + i)),
        (*(*(mtrx + k) + i)) = (*(*(mtrx + i) + k)),
        (*(*(mtrx + i) + k)) = temp;
    }
}

int main(void) {
    char sbuff[MAXLINE + 1];
    unsigned *ip, i, mtrx_size, swipe_idx;
    double *dp, randlow, randhigh;

    srand((unsigned)time(NULL));

    for (i = 0; i < 2; ++i) {
        printf("enter (col & row) ");
        switch (i) {
        case 0:
            ip = &mtrx_size;
            printf("num: ");
            break;
        case 1:
            ip = &swipe_idx;
            printf("swipe: ");
        }
        getline_(sbuff, MAXLINE);
        while (!is_num(sbuff, 0)) {
            printf("try again: ");
            getline_(sbuff, MAXLINE);
        }
        *ip = atoi(sbuff);
    }

    for (i = 0; i < 2; ++i) {
        printf("enter ");
        switch (i) {
        case 0:
            dp = &randlow;
            printf("low: ");
            break;
        case 1:
            dp = &randhigh;
            printf("high: ");
        }
        getline_(sbuff, MAXLINE);
        while (!is_num(sbuff, 1)) {
            printf("try again: ");
            getline_(sbuff, MAXLINE);
        }
        *dp = atof(sbuff);
    }

    float mtrx[mtrx_size][mtrx_size];
    init_mrtx(mtrx_size, mtrx, randlow, randhigh);
    printf("default matrix:\n");
    print_mtrx(mtrx_size, mtrx);
    swap_rowtocolumn(swipe_idx, mtrx_size, mtrx);
    printf("transform:\n");
    print_mtrx(mtrx_size, mtrx);
    return 0;
}
