// checking whether a number was entered or not a number

#include <stdio.h>

#define MAX_LENGTH 100

int is_digit(char c) { return c >= '0' && c <= '9'; }

int is_num(char s[], char is_float, char is_neg) {
    char f = 0; // was there a dot in the line before
    int i = 0;
    while (s[i] != '\0') {
        if (!(is_digit(s[i]) || (s[i] == '.' && !f && is_float) ||
              (s[i] == '-' && i == 0 && is_neg))) {
            return 0;
        }
        if (s[i] == '.') {
            f = 1;
        }
        ++i;
    }
    if (i == 0 || (i == 1 && (s[0] == '.' || s[0] == '-')))
        return 0;
    return 1;
}

float atof(char s[]) {
    int res = 0;
    int pow = 0;
    char minus = 0;
    int i = 0;
    if (s[i] == '-' || s[i] == '+') {
        if (s[i] == '-') {
            minus = 1;
        }
        ++i;
    }
    for (; is_digit(s[i]) || s[i] == '.'; ++i) {
        if (s[i] == '.') {
            pow = 1;
            continue;
        }
        res = res * 10 + s[i] - '0';
        pow *= 10;
    }
    return (float)((minus ? -1 : 1) * res) / (float)(pow ? pow : 1);
}

int get_line(char buff_s[], int lim) {
    int i = 0;
    while (i < lim && (buff_s[i] = (char)getchar()) != EOF &&
           buff_s[i] != '\n') {
        ++i;
    }
    buff_s[i] = '\0';
    return i;
}

int main() {
    char s[MAX_LENGTH + 1];
    float num;

    printf("enter a number:\n");
    for (;;) {
        get_line(s, MAX_LENGTH);
        if (is_num(s, 1, 1)) {
            break;
        }
        printf("try again:\n");
    }
    num = atof(s);
    printf("num = %f\nnum + 1 = %f", num, num + 1);
}
