#include <stdio.h>

int pow_(int base, unsigned power) {
    int res = 1;
    do {
        if (power & 1u) {
            res *= base;
        }
        base *= base;
    } while ((power >>= 1) > 0);
    return res;
}

int main() { printf("%d", pow_(-3, 5)); }
