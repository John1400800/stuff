#include <stdio.h>

#define ZERO_FAHR 273

int main(void) {
    int n = 1, i = 2, t_c = 18; 
    long double k = (8.617333262e-5);
    long double e = n * i / 2.l * k * (ZERO_FAHR + t_c);
    printf("%Lf ( W * m^(−2) * K^(−4) )", e);
}
