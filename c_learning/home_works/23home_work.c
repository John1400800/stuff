#include <stdio.h>

#define ZERO_FAHR 273
#define BOLTZMANN_CONST 8.617333262e-5

int main(void) {
    int n = 1, i = 2, t_c = 18;
    long double e;
    printf("( W * m^(−2) * K^(−4) )\n%Lf ",
           e = n * i / 2 * BOLTZMANN_CONST * (ZERO_FAHR + t_c));
}
