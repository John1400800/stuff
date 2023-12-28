#include <ctype.h>
#include <stdio.h>

#define MAXLINE 100

char get_num(char *buff, unsigned lim) {
    unsigned i = 0;
    char is_dig = 1;
    while (i < lim && (buff[i] = (char)getchar()) != '\n') {
        if (!(isdigit(buff[i]) || (buff[i] == '-' && i == 0))) {
            is_dig = 0;
        }
        ++i;
    }
    buff[i] = '\0';
    if (i == 0 || (i == 1 && buff[0] == '-')) {
        return 0;
    }
    return is_dig;
}

int atoi(char *num) {
    int res = 0;
    unsigned i = 0;
    char is_minus = 0;
    if (num[i] == '-' || num[i] == '+') {
        if (num[i] == '-') {
            is_minus = 1;
        }
        ++i;
    }
    while (num[i] >= '0' && num[i] <= '9') {
        res = res * 10 + (int)(num[i]) - '0';
        ++i;
    }
    return is_minus ? -res : res;
}

unsigned long fact(int n) {
    if (n < 0) {
        return 0;
    } else if (n == 1 || n == 0)
        return 1;
    unsigned long res = 1;
    while (n >= 2) {
        res *= (unsigned)(n--);
    }
    return res;
}

int main() {
    char buff_s[MAXLINE + 1];
    int num;
    unsigned fact_of_num;
    printf("enter a number: ");
    while (!get_num(buff_s, MAXLINE)) {
        printf("invalid input, try again: ");
    }
    // printf("number: %d\n", (num = atoi(buff_s)));
    fact_of_num = fact(num = atoi(buff_s));
    if (fact_of_num) {
        printf("%d! = %d\n", num, fact_of_num);
    } else {
        printf("%d hasn't factorial :( \n", num);
    }
}