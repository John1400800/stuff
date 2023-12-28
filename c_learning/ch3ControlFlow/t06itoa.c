#include <limits.h>
#include <stdio.h>

void str_copy(char *source, char *buffer) {
    unsigned i = 0;
    while ((buffer[i] = source[i]) != '\0')
        ++i;
}

int min = INT_MIN;

unsigned str_len(char *s) {
    unsigned i = 0;
    while (s[i] != '\0') {
        ++i;
    }
    return i;
}

void reverse(char *s) {
    char buff;
    unsigned low, high;
    for (low = 0, high = str_len(s) - 1; low < high; ++low, --high) {
        buff = s[low];
        s[low] = s[high];
        s[high] = buff;
    }
}

void itoa(int number, char *res) {
    if (number == INT_MIN) {          // When converting to a positive value,
        str_copy("-2147483648", res); // an overflow occurs
        return;
    }
    int minus;
    unsigned i;
    minus = number < 0 ? number *= -1, 1 : 0;
    i = 0;
    do {
        res[i++] = '0' + number % 10;
    } while ((number /= 10) > 0);
    if (minus) {
        res[i++] = '-';
    }
    res[i] = '\0';
    reverse(res);
}

int main(void) {
    char s[100];
    itoa(-2147483648, s);
    printf("%s", s);
}
