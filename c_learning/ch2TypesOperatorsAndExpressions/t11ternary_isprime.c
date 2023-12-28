#include <stdio.h>

char is_prime(unsigned n) {
    if (n < 2) 
        return 0;
    for (unsigned m = 2; m * m <= n; ++m) {
        if (n % m == 0)
            return 0;
    }
    return 1;
}

int main() {
    for (int i = 0, n = 1; n < 1000; ++n) {
        if (is_prime(n)) {
            printf("%3d%c", n, i % 8 == 7 ? '\n' : ' ');
            ++i;
        }
    }
}