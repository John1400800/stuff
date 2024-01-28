#include <math.h>
#include <stdio.h>


#define EPS 1e-4
#define EULERS_NUM 2.7182818284590452
#define abs(a) ((a) < 0 ? -(a) : (a))

unsigned fact(unsigned n) {
    unsigned res = 1;
    while (n > 1) {
        res *= n;
        --n;
    }
    return res;
}

int main(void) {
    double sum, term;
    unsigned x, n;
    x = 2;

    sum = 0;
    n = 0;
    while ((term = pow(x, 2 * n + 1) / fact(2 * n + 1)) > EPS) {
        sum += term;
        ++n;
    }

    sum = 0;
    n = 0;
    term = 0;
    do {
        sum += term;
        term = pow(x, 2 * n + 1) / fact(2 * n + 1);
        ++n;
    } while (term > EPS);

    printf("%lf %fl\n", sum,
           (pow(EULERS_NUM, x) - pow(EULERS_NUM, -(double)(x))) / 2.);
    printf(
        "%lf\n",
        abs(sum - (pow(EULERS_NUM, x) - pow(EULERS_NUM, -(double)(x))) / 2.));
    return 0;
}
