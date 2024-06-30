#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

static const char digits[] = "0123456789abcdef";

void itob(int64_t n, char *resptr, size_t base);

int main(void) {
    char buff[10];
#define TEST_NUM 117
#define BASE 2
    itob(TEST_NUM, buff, BASE);
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
    for (rem=1u; n/rem>=base; rem*=base)
        ;
    for (i=0; !i || rem; n%=rem, rem/=base, ++i)
        resptr[i] = digits[n/rem];
    resptr[i] = '\0';
}
