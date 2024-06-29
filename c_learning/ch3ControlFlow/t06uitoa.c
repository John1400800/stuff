#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

static const char digits[] = "0123456789abcdef";

void itob(int64_t n, char *resptr, size_t base);

int main(void) {
    char buff[10];
#define TEST_NUM 255
    itob(TEST_NUM, buff, 16);
    printf( "input number: %d\n"
            "result:       %s\n",
            TEST_NUM, buff );
    return EXIT_SUCCESS;
}

void utob(uint64_t n, char *resptr, size_t base);

void itob(int64_t n, char *resptr, size_t base) {
    if (n < 0) {
        n = -n;
        *resptr++ = '-';
    }
    utob((uint64_t)n, resptr, base);
}

void utob(uint64_t n, char *resptr, size_t base) {
    size_t i, rem;
    for (i=1, rem=base; n/rem > 0; ++i)
        rem *= base;
    resptr[i] = '\0';
    while (i > 0) {
        resptr[--i] = digits[n % base];
        n /= base;
    }
}
