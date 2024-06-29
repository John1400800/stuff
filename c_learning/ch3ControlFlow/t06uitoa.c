#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#define TEST_NUM -134

void itoa(int64_t n, char *resptr);

int main(void) {
    char buff[10];
    itoa(TEST_NUM, buff);
    printf( "input number: %d\n"
            "result:       %s\n",
            TEST_NUM, buff);
    return EXIT_SUCCESS;
}

void utoa(uint64_t n, char *resptr);

void itoa(int64_t n, char *resptr) {
    if (n < 0) {
        n = -n;
        *resptr++ = '-';
    }
    utoa((uint64_t)n, resptr);
}

void utoa(uint64_t n, char *resptr) {
    size_t i, rem;
    for (i=1, rem=10; n/rem > 0; ++i)
        rem *= 10;
    resptr[i] = '\0';
    while (i > 0) {
        resptr[--i] = (char)(n % 10) + '0';
        n /= 10;
    }
}
