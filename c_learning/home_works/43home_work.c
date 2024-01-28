#include <stdio.h>

#define GAS_CONSTANT      8.31446261815324
#define ZERO_CELS_IN_KELV 273.15

#define VOLUME            (480 / 1e-6)
#define PRESSURE          2.5e4
#define LOW_T             10
#define HIGH_T            20

int main(void) {
    unsigned cels;
    for (cels = 10; cels <= 20; ++cels) {
        printf("%u°С - %lf\n", cels,
               (PRESSURE * VOLUME) /
                   (GAS_CONSTANT * (ZERO_CELS_IN_KELV + cels)));
    }
    return 0;
}
