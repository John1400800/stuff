#include <stdio.h>

char *uitoa(int n, char *str);

int main(void) {
    char buff[100];
    printf("%s\n", uitoa(145, buff));
}

char *uitoa(int n, char *str) {
    char *ptr;
    int divisor;
    for (divisor=1; n/divisor>=10; divisor*=10)
        ;
    for (ptr = str; divisor>0; ++ptr, n%=divisor, divisor/=10)
        *ptr = (char)('0'+n/divisor);
    *ptr = '\0';
    return str;
}
