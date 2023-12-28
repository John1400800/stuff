#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#ifndef isdigit
#define isdigit(c) ((c) >= '0' && (c) <= '9')
#endif

#ifndef swap
#define swap(t, a, b)                                                          \
    t temp = (a);                                                              \
    (a) = (b);                                                                 \
    (b) = temp
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

void rand_init_mrtx(unsigned size, float mtrx[][size], int rlow, int rhigh) {
    unsigned i, j;
    for (i = 0; i < size; ++i) {
        for (j = 0; j < size; ++j) {
            mtrx[i][j] = frand(rlow, rhigh);
        }
    }
}

void init_mrtx(unsigned size, float mtrx[][size], int rlow, int rhigh) {
    unsigned i, j;
    for (i = 0; i < size; ++i) {
        for (j = 0; j < size; ++j) {
            mtrx[i][j] = (10+tan(i+2j))/(sqrt(j)+4);
        }
    }
}

void mul(float a[][3], float b[][3], float c[][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            c[i][j] = 0;
            for (int k = 0; k < 3; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

void print_mtrx(unsigned size, float mtrx[][size]) {
    unsigned i, j;
    for (i = 0; i < size; ++i) {
        putchar('|');
        for (j = 0; j < size; ++j) {
            printf("%5.2f", mtrx[i][j]);
            putchar('|');
        }
        putchar('\n');
    }
    putchar('\n');
}

void swap_row_column(unsigned k, unsigned size, float (*mtrx)[size]) {
    unsigned i;
    float temp;
    for (i = 0; i < size; ++i) {
        if (i == k)
            continue;
        swap(float, mtrx[k][i], mtrx[i][k]);
    }
}

int invert(float a[][3], float inv[][3]) {
    inv[0][0] = a[1][1] * a[2][2] - a[1][2] * a[2][1];
    inv[0][1] = a[0][2] * a[2][1] - a[0][1] * a[2][2];
    inv[0][2] = a[0][1] * a[1][2] - a[0][2] * a[1][1];
    inv[1][0] = a[1][2] * a[2][0] - a[1][0] * a[2][2];
    inv[1][1] = a[0][0] * a[2][2] - a[0][2] * a[2][0];
    inv[1][2] = a[0][2] * a[1][0] - a[0][0] * a[1][2];
    inv[2][0] = a[1][0] * a[2][1] - a[1][1] * a[2][0];
    inv[2][1] = a[0][1] * a[2][0] - a[0][0] * a[2][1];
    inv[2][2] = a[0][0] * a[1][1] - a[0][1] * a[1][0];

    float det = a[0][0] * inv[0][0] + a[0][1] * inv[1][0] + a[0][2] * inv[2][0];
    
    if (det == 0)
        return 0;

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            inv[i][j] /= det;

    return 1;
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
    rand_init_mrtx(mtrx_size, mtrx, randlow, randhigh);
    printf("default matrix:\n");
    print_mtrx(mtrx_size, mtrx);
    swap_rowtocolumn(swipe_idx, mtrx_size, mtrx);
    printf("transform:\n");
    print_mtrx(mtrx_size, mtrx);
    return 0;
}
