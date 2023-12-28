#include <stdio.h>

unsigned char is_leap_year(unsigned year) {
    return year % 4 == 0 && year % 100 != 0 || year % 400 == 0;
}

void str_copy(char *source, char *buff) {
    unsigned i = 0;
    while ((buff[i] = source[i]) != '\0') {
        ++i;
    }
}

int main() {
    unsigned year = 2016;
    char is_leap[100];
    str_copy(is_leap_year(year) ? "really" : "it's not true", is_leap);
    //                                 ???
    printf("%d leap year\n%s", year, is_leap);
}
