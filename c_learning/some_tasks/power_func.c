#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

#define MAX_LENGTH 100

static const char digits[] = "0123456789abcdef";

// проверяет ли явдяется c числом в сс с основ base
int base_placed(char c, unsigned base) {
    int state = ((c >= '0' && c <= (base < 10 ? digits[base - 1] : '9')) ||
                 (base > 10 && c >= digits[10] && c <= digits[base - 1]));
    return state;
}

/* writes a line to num[] and returns 1 if a number is entered,
if a non-number is entered returns 0 */
int get_num(char num[], int lim, int is_negative, int is_float, unsigned base) {
    int i = 0;
    int is_dot = 0;
    int is_digit = 1;
    while (i < lim && (num[i] = (char)getchar()) != EOF && num[i] != '\n') {
        if (!(base_placed(num[i], base) ||
              (num[i] == '.' && !is_dot && is_float) ||
              (((num[i] == '-' && is_negative) || num[i] == '+') && i == 0))) {
            is_digit = 0;
        }
        if (num[i] == '.') {
            is_dot = 1;
        }
        ++i;
    }
    num[i] = '\0';
    if (i == 0) {
        is_digit = 0;
    }
    return is_digit;
}

int anegtopos(char s[]) {
    if (s[0] == '-' || s[0] == '+') {
        s[0] = '0';
        return s[0] == '-' ? -1 : 1;
    }
    return 1;
}

unsigned btou(char num[], unsigned base) {
    unsigned res = 0;
    int i = 0;
    while ((num[i] >= '0' && num[i] <= '9') ||
           (num[i] >= 'a' && num[i] <= 'z')) {
        res = res * base + (unsigned)((num[i] >= '0' && num[i] <= '9')
                                          ? num[i] - '0'
                                          : num[i] - 'a' + 10);
        ++i;
    }
    return res;
}

int power(int base, unsigned pow) {
    int res = 1;
    do {
        if (pow & 1u) {
            res *= base;
        }
        base *= base;
    } while (pow >>= 1);
    return res;
}

/* перевод введеного числа в введенное основание
 сначала вводится последнее */
void foo1() {
    char num[MAX_LENGTH + 1];
    unsigned base;
    int res_sign;

    printf("enter the base:\n");
    while (!get_num(num, MAX_LENGTH, 0, 0, 10u)) {
        printf("try  again:\n");
    }
    base = btou(num, 10u);
    printf("enter a number on a base system:\n");
    while (!get_num(num, MAX_LENGTH, 1, 0, base)) {
        printf("try again:\n");
    }
    res_sign = anegtopos(num);
    printf("%d", (int)btou(num, base) * res_sign);
}

/* вводите основание а затем степент аозвращает результат возведения в степень
 */
void foo2() {
    char num[MAX_LENGTH + 1];
    int base_sign;
    int base;
    unsigned power;

    printf("enter a base:\n");
    while (!get_num(num, MAX_LENGTH, 1, 0, 10u)) {
        printf("try again:\n");
    }

    base_sign = anegtopos(num);
    base = base_sign * (int)btou(num, 10);

    printf("enter a power:\n");
    while (!get_num(num, MAX_LENGTH, 0, 0, 10u)) {
        printf("try again:\n");
    }

    power = btou(num, 10);
    printf("%d", pow_(base, power));
}

int main() { foo2(); }
