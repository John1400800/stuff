#include <stdio.h>

#define NUM_EL 100000

void sieve_of_eratosthenes(void) {
    unsigned i, j, cnt = 1, prime[NUM_EL + 1];

    for (i = 2; i <= NUM_EL; ++i) {
        prime[i] = 1;
    }

    printf("| ");                                                        // print

    for (i = 2; i <= NUM_EL; ++i) {
        if (prime[i] == 0) {
            continue;
        }

        printf("%5d |%s", i, cnt % 8 == 0 && i != 99991 ? "\n| " : " "); // print
        ++cnt;                                                           // print

        for (j = i * i; j <= NUM_EL; j += i) {
            prime[j] = 0;
        }
    }
}

int main(void) {
    sieve_of_eratosthenes();
    return 0;
}
