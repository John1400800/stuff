// absolutely dumb way to use global variables
// to print longest line

#include <stdio.h>

#define MAX_LENGTH 100

char str[MAX_LENGTH + 1];
char max_str[MAX_LENGTH + 1];

int get_line(void);
void str_copy(void);

int main() {
    int max_len = 0;
    int len;
    while ((len = get_line()) > 0) {
        if (len > max_len) {
            str_copy();
            max_len = len;
        }
    }
    if (max_len > 0) {
        printf("%s", max_str);
    }
}

void str_copy(void) {
    int i = 0;
    while ((max_str[i] = str[i]) != '\0') {
        ++i;
    }
}

int get_line(void) {
    int i;
    for (i = 0;
         i < MAX_LENGTH && (str[i] = (char)getchar()) != '\n' && str[i] != EOF;
         ++i)
        ;
    str[i] = '\n';
    return i;
}
